import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection
from clickhouse_sqlalchemy.alembic.dialect import patch_alembic_version, include_object
from alembic import context
from asynch.errors import NotSupportedError

import app.models.clickhouse # noqa
from app.core.config import settings
from app.core.db.clickhouse import Base, clickhouse_engine



# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
config.set_main_option('sqlalchemy.url', settings.clickhouse_settings.dsn.unicode_string())


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        patch_alembic_version(context)
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        patch_alembic_version(context)
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    async with clickhouse_engine.connect() as connection:
        try:
            context.configure(
                connection=connection, target_metadata=target_metadata,
                include_object=include_object,
            )
            await connection.run_sync(do_run_migrations)
        except NotSupportedError: # Игнорирование исключений ClickHouse по транзакциям.
            pass

    await clickhouse_engine.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
