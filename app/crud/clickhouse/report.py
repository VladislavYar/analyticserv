from app.models.clickhouse.report import ReportModel
from app.crud.clickhouse.base import CRUDBase


class CRUDReport(CRUDBase):
    """CRUD Report."""

    model = ReportModel
