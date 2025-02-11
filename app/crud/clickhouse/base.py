from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.clickhouse.abstract import ClickhouseModel


class CRUDBase:
    """Базовый класс реализациия CRUD операций."""

    model: ClickhouseModel

    async def create(self, session: AsyncSession, data: dict[str, Any]) -> None:
        """Создание записи.

        Args:
            session (AsyncSession): сессия ClickHouse.
            data (dict[str, Any]): данные для сохранения.
        """
        obj = self.model(**{key: value for key, value in data.items() if key in self.model.__dict__ and value})
        session.add(obj)
        await session.flush()
