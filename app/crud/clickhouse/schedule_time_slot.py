from app.models.clickhouse.schedule_time_slot import ScheduleTimeSlotModel
from app.crud.clickhouse.base import CRUDBase


class CRUDScheduleTimeSlot(CRUDBase):
    """CRUD ScheduleTimeSlot."""

    model = ScheduleTimeSlotModel
