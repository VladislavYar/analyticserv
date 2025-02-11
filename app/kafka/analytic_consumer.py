

from typing import Any
import json

from aiokafka import AIOKafkaConsumer

from app.core.db.clickhouse import get_clickhouse_async_session
from app.core.config import settings
from app.constants import ServicesNameMap, EventTypeMap, UNKNOWN
from app.crud.clickhouse.base import CRUDBase
from app.crud.clickhouse.answer import CRUDReportAnswer
from app.crud.clickhouse.event import CRUDEvent
from app.crud.clickhouse.level import CRUDLevel
from app.crud.clickhouse.level_value import CRUDLevelValue
from app.crud.clickhouse.report import CRUDReport
from app.crud.clickhouse.schedule_time_slot import CRUDScheduleTimeSlot


class AnalyticConsumer:
    """Consumer обработки сообщений аналитики.

    Attributes:
        CRUD_MAP (dict[str, CRUDBase]): MAP CRUD моделей ClickHouse.
    """

    CRUD_MAP: dict[str, CRUDBase] = {
        'report': CRUDReport,
        'schedule': CRUDScheduleTimeSlot,
        'report_answer': CRUDReportAnswer,
        'level_value': CRUDLevelValue,
        'level': CRUDLevel,
    }

    async def start(self) -> None:
        """Запуск цикла consumer-a."""
        dsn = settings.kafka_settings.dsn
        query_params = dict(dsn.query_params())
        consumer = AIOKafkaConsumer(
            query_params.pop('topic'),
            bootstrap_servers=f'{dsn.host}:{dsn.port}',
            **query_params,
        )
        await consumer.start()
        try:
            async for message in consumer:
                if not message.value:
                    continue
                await self.save_message(json.loads(message.value))
        finally:
            await consumer.stop()

    async def save_message(self, data: dict[str, Any]) -> None:
        """Сохранение данных из сообщения.

        Args:
            data (dict[str, Any]): данные для сохранения.
        """
        data['service'] = ServicesNameMap[data['service']]
        event_type = EventTypeMap.get(data['event_type'], EventTypeMap[UNKNOWN])
        data['event_type'] = event_type
        async for session in get_clickhouse_async_session():
            await self.CRUD_MAP[data.get('instance_name')](session).create(data)
            await CRUDEvent(session).create(data)
