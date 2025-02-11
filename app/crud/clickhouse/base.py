from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.clickhouse.abstract import ClickhouseModel


class CRUDBase:
    """Базовый класс реализациия CRUD операций."""

    model: ClickhouseModel

    def __init__(self, session: AsyncSession) -> None:
        """Инициализация CRUD модели.

        Args:
            session (AsyncSession): сессия ClickHouse.
        """
        self._session = session

    async def create(self, data: dict[str, Any]) -> None:
        """Создание записи.

        Args:
            data (dict[str, Any]): данные для сохранения.
        """
        obj = self.model(**{key: value for key, value in data.items() if key in self.model.__dict__ and value})
        self._session.add(obj)
        await self._session.flush()
