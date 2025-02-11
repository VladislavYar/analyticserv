from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationInfo, field_validator
from pydantic.networks import PostgresDsn, RedisDsn, KafkaDsn, ClickHouseDsn


class Base(BaseSettings):
    """Базовая конфигурация настроек."""

    model_config = SettingsConfigDict(
        extra='allow', env_file='.env', env_file_encoding='utf-8'
        )


class AppSettings(Base):
    """Настройки приложения."""

    asgi_app_path: str = 'app.main:app'
    asgi_host: str = '127.0.0.1'
    asgi_port: int = 8126
    asgi_reload: bool = False
    service_token: str | None = None
    serive_name: str = 'Analytic'

    model_config = SettingsConfigDict(env_prefix='APP_')


class PostgresSettings(Base):
    """Настройки postgres."""

    protocol: str = 'postgresql+asyncpg'
    host: str = '127.0.0.1'
    port: int = 5432
    db_name: str = 'analytic'
    username: str = 'postgres'
    password: str = 'postgres'
    dsn: PostgresDsn | None = None

    model_config = SettingsConfigDict(env_prefix='POSTGRES_')

    @field_validator('dsn', mode='before')
    def validate_dsn(cls,  value: PostgresDsn | None, info: ValidationInfo) -> PostgresDsn:
        """Валидация postgres dsn.

        Args:
            value (PostgresDsn | None): значение.
            info (ValidationInfo): данные валидации.

        Returns:
            PostgresDsn: postgres dsn.
        """
        if value:
            return value
        data = info.data
        return PostgresDsn(
         f'{data['protocol']}://{data['username']}:{data['password']}@{data['host']}:{data['port']}/{data['db_name']}'
        )


class ClickHouseSettings(Base):
    """Настройки clickhouse."""

    protocol: str = 'clickhouse+asynch'
    host: str = '127.0.0.1'
    port: int = 9000
    db_name: str = 'analytic'
    username: str = 'default'
    password: str = ''
    dsn: ClickHouseDsn | None = None

    model_config = SettingsConfigDict(env_prefix='CLICKHOUSE_')

    @field_validator('dsn', mode='before')
    def validate_dsn(cls,  value: ClickHouseDsn | None, info: ValidationInfo) -> ClickHouseDsn:
        """Валидация clickhouse dsn.

        Args:
            value (ClickHouseDsn | None): значение.
            info (ValidationInfo): данные валидации.

        Returns:
            ClickHouseDsn: clickhouse dsn.
        """
        if value:
            return value
        data = info.data
        return ClickHouseDsn(
         f'{data['protocol']}://{data['username']}:{data['password']}@{data['host']}:{data['port']}/{data['db_name']}',
        )


class RedisSettings(Base):
    """Настройки redis."""

    protocol: str = 'redis'
    host: str = '127.0.0.1'
    port: int = 6379
    db_name: str = '10'
    username: str = 'default'
    dsn: RedisDsn | None = None

    model_config = SettingsConfigDict(env_prefix='REDIS_')

    @field_validator('dsn', mode='before')
    def validate_dsn(cls,  value: RedisDsn | None, info: ValidationInfo) -> RedisDsn:
        """Валидация redis dsn.

        Args:
            value (RedisDsn | None): значение.
            info (ValidationInfo): данные валидации.

        Returns:
            RedisDsn: redis dsn.
        """
        if value:
            return value
        data = info.data
        return RedisDsn(
         f'{data['protocol']}://{data['username']}@{data['host']}:{data['port']}/{data['db_name']}'
        )


class KafkaSettings(Base):
    """Настройки kafka."""

    protocol: str = 'kafka'
    host: str = '127.0.0.1'
    port: int = 9092
    topic: str = 'madirect.analytic'
    username: str = ''
    password: str = ''
    dsn: KafkaDsn | None = None

    model_config = SettingsConfigDict(env_prefix='KAFKA_')

    @field_validator('dsn', mode='before')
    def validate_dsn(cls,  value: KafkaDsn | None, info: ValidationInfo) -> KafkaDsn:
        """Валидация clickhouse dsn.

        Args:
            value (ClickHouseDsn | None): значение.
            info (ValidationInfo): данные валидации.

        Returns:
            KafkaDsn: clickhouse dsn.
        """
        if value:
            return value
        data = info.data
        return KafkaDsn(
         f'{data['protocol']}://{data['username']}:{data['password']}@'
         f'{data['host']}:{data['port']}?topic={data['topic']}'
        )


class Settings(BaseSettings):
    """Настройки."""

    app_settings: AppSettings = AppSettings()
    postgres_settings: PostgresSettings = PostgresSettings()
    clickhouse_settings: ClickHouseSettings = ClickHouseSettings()
    redis_settings: RedisSettings = RedisSettings()
    kafka_settings: KafkaSettings = KafkaSettings()


settings: Settings = Settings()
