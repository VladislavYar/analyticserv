
from sqlalchemy import Column
from clickhouse_sqlalchemy.types import UInt64, UInt32, Nullable

from app.models.clickhouse.abstract import ClickhouseModel


class EventModel(ClickhouseModel):
    """Модель Event."""

    user__id = Column(Nullable(UInt32))
    company__id = Column(Nullable(UInt32))
    project__id = Column(Nullable(UInt32))
    project_scheme__id = Column(Nullable(UInt32))
    project_territory__id = Column(Nullable(UInt32))
    level__id = Column(Nullable(UInt64))
    level_value__id = Column(Nullable(UInt64))
    geo_point__id = Column(Nullable(UInt32))
    schedule_time_slot__id = Column(Nullable(UInt32))
    worker_report__id = Column(Nullable(UInt32))
    processed_report__id = Column(Nullable(UInt32))
    processed_report_element__id = Column(Nullable(UInt32))
