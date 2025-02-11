from app.models.clickhouse.event import EventModel
from app.crud.clickhouse.base import CRUDBase


class CRUDEvent(CRUDBase):
    """CRUD Event."""

    model = EventModel
