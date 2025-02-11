from sqlalchemy import Column
from clickhouse_sqlalchemy.types import UInt8, UInt64, UInt32, Nullable, String, Float32

from app.core.db.clickhouse import Base


class ClickhouseModel(Base):
    """Базовая модель ClickHouse."""

    __abstract__ = True

    instance_id = Column(Nullable(UInt32))
    instance_name = Column(Nullable(String))
    service = Column(UInt8)  # madirect_prod / service_stage / service_dev / maworks
    event_type = Column(Nullable(UInt32))


class AbstractCompanyModel(Base):
    """Абстрактная модель Company."""

    __abstract__ = True

    company__id = Column(Nullable(UInt32))
    company__title = Column(Nullable(String))


class AbstractTerritoryModel(Base):
    """Абстрактная модель Territory."""

    __abstract__ = True

    territory__id = Column(Nullable(UInt32))
    territory__title = Column(Nullable(String))


class AbstractProjectModel(Base):
    """Абстрактная модель Project."""

    __abstract__ = True

    project__id = Column(Nullable(UInt32))
    project__title = Column(Nullable(String))


class AbstractProjectSchemeModel(Base):
    """Абстрактная модель ProjectScheme."""

    __abstract__ = True

    project_scheme__id = Column(Nullable(UInt32))
    project_scheme__title = Column(Nullable(String))
    project_scheme__report_creation_radius = Column(Nullable(UInt32))
    project_scheme__report_creation_duration = Column(Nullable(UInt32))


class AbstractProjectTerritoryModel(Base):
    """Абстрактная модель ProjectTerritory."""

    __abstract__ = True

    project_territory__id = Column(Nullable(UInt32))
    project_territory__reward = Column(Nullable(UInt32))
    project_territory__created_at = Column(Nullable(UInt32))


class AbstractGeoPointModel(Base):
    """Абстрактная модель GeoPoint."""

    __abstract__ = True

    geo_point__id = Column(Nullable(UInt32))
    geo_point__title = Column(Nullable(String))
    geo_point__reward = Column(Nullable(UInt32))
    geo_point__lat = Column(Nullable(Float32))
    geo_point__lon = Column(Nullable(Float32))
    geo_point__city = Column(Nullable(String))
    geo_point__address = Column(Nullable(String))
    geo_point__created_at = Column(Nullable(UInt32))


class AbstractScheduleTimeSlotModel(Base):
    """Абстрактная модель ScheduleTimeSlot."""

    __abstract__ = True

    schedule_time_slot__id = Column(Nullable(UInt32))
    schedule_time_slot__reward = Column(Nullable(UInt32))
    schedule_time_slot__max_reports_qty = Column(Nullable(UInt32))
    schedule_time_slot__max_reports_qty_per_day = Column(Nullable(UInt32))
    schedule_time_slot__max_reports_qty_per_worker = Column(Nullable(UInt32))
    schedule_time_slot__max_reports_qty_per_worker_day = Column(Nullable(UInt32))
    schedule_time_slot__active_since_local = Column(Nullable(UInt64))
    schedule_time_slot__active_till_local = Column(Nullable(UInt64))
    schedule_time_slot__active_since = Column(Nullable(UInt64))
    schedule_time_slot__active_till = Column(Nullable(UInt64))
    schedule_time_slot__created_at = Column(Nullable(UInt64))


class AbstractCompanyUserModel(Base):
    """Абстрактная модель CompanyUser."""

    __abstract__ = True

    company_user__id = Column(Nullable(UInt32))


class AbstractWorkerReportCompanyUserModel(Base):
    """Абстрактная модель WorkerReportCompanyUser."""

    __abstract__ = True

    worker_report__company_user__id = Column(Nullable(UInt32))


class AbstractUserModel(Base):
    """Абстрактная модель User."""

    __abstract__ = True

    user__id = Column(Nullable(UInt32))
    user__first_name = Column(Nullable(String))
    user__middle_name = Column(Nullable(String))
    user__last_name = Column(Nullable(String))
    user__phone = Column(Nullable(UInt64))


class AbstractWorkerReportUserModel(Base):
    """Абстрактная модель WorkerReportUser."""

    __abstract__ = True

    worker_report__user__id = Column(Nullable(UInt32))
    worker_report__user__first_name = Column(Nullable(String))
    worker_report__user__middle_name = Column(Nullable(String))
    worker_report__user__last_name = Column(Nullable(String))
    worker_report__user__phone = Column(Nullable(UInt64))


class AbstractWorkerReportModel(Base):
    """Абстрактная модель WorkerReport."""

    __abstract__ = True

    worker_report__id = Column(Nullable(UInt32))
    worker_report__status = Column(Nullable(String))
    worker_report__start_at = Column(Nullable(UInt64))
    worker_report__loaded_at = Column(Nullable(UInt64))
    worker_report__finish_at = Column(Nullable(UInt64))


class AbstractProcessedReportModel(Base):
    """Абстрактная модель ProcessedReport."""

    __abstract__ = True

    processed_report__id = Column(Nullable(UInt32))
    processed_report__status = Column(Nullable(String))
    processed_report__partner_status = Column(Nullable(UInt32))


class AbstractProcessedReportElementModel(Base):
    """Абстрактная модель ProcessedReportElement."""

    __abstract__ = True

    processed_report_element__id = Column(Nullable(UInt32))
    processed_report_element__branch_id = Column(Nullable(String))
    processed_report_element__status = Column(Nullable(String))


class AbstractLevelModel(Base):
    """Абстрактная модель Level."""

    __abstract__ = True

    level__id = Column(Nullable(UInt64))
    level__title = Column(Nullable(String))
    level__nesting_level = Column(Nullable(UInt64))


class AbstractLevelValueModel(Base):
    """Абстрактная модель LevelValue."""

    __abstract__ = True

    level_value__id = Column(Nullable(UInt64))
    level_value__level__id = Column(Nullable(UInt64))
    level_value__title = Column(Nullable(String))
    level_value__path = Column(Nullable(String))
