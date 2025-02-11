from typing import AsyncGenerator
import re

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from clickhouse_sqlalchemy.ext.declarative import declarative_base
from clickhouse_sqlalchemy import make_session
from sqlalchemy.ext.declarative import declared_attr
from clickhouse_sqlalchemy.types import UInt64
from sqlalchemy import Column
from clickhouse_sqlalchemy import engines

from app.core.config import settings


REG_WORD_SEPARATION_IN_CAMEL_CASE = r'(?<!^)(?=[A-Z])'


class PreBase:
    """Кастомизация базовой модели."""

    # primary_key=True для работоспособности Alembic. Само поле может быть не уникальным.
    happen_at = Column(UInt64, primary_key=True)

    # В Alembic движки в миграциях нужно прописывать самостоятельно.
    __table_args__ = (
        engines.MergeTree(order_by=('happen_at',)),
    )

    @declared_attr
    def __tablename__(cls) -> str:
        """Автоматическая генерация названия таблицы.

        Returns:
            str: название таблицы.
        """
        return re.sub(REG_WORD_SEPARATION_IN_CAMEL_CASE, '_', cls.__name__).lower().replace('_model', '')


Base = declarative_base(cls=PreBase)
clickhouse_engine = create_async_engine(settings.clickhouse_settings.dsn.unicode_string())


async def get_clickhouse_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Генератор ассинхронных сессий.

    Returns:
        AsyncSession: ассинхронная сессия.

    Yields:
        Iterator[AsyncSession]: ассинхронная сессия.
    """
    async with make_session(clickhouse_engine, is_async=True) as async_session:
        yield async_session
