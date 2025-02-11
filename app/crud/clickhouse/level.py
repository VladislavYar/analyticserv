from app.models.clickhouse.level import LevelModel
from app.crud.clickhouse.base import CRUDBase


class CRUDLevel(CRUDBase):
    """CRUD Level."""

    model = LevelModel
