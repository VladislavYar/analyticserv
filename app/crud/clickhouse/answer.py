from app.models.clickhouse.answer import ReportAnswerModel
from app.crud.clickhouse.base import CRUDBase


class CRUDReportAnswer(CRUDBase):
    """CRUD ReportAnswer."""

    model = ReportAnswerModel
