from app.models.clickhouse.level_value import LevelValueModel
from app.crud.clickhouse.base import CRUDBase


class CRUDLevelValue(CRUDBase):
    """CRUD LevelValue."""

    model = LevelValueModel
