
from sqlalchemy import Column
from clickhouse_sqlalchemy.types import UInt32, Nullable, String

from app.models.clickhouse.abstract import (
    ClickhouseModel, AbstractScheduleTimeSlotModel, AbstractCompanyModel,
    AbstractTerritoryModel, AbstractProjectTerritoryModel, AbstractProjectSchemeModel,
    AbstractGeoPointModel, AbstractLevelModel, AbstractLevelValueModel, AbstractProjectModel,
    AbstractProcessedReportElementModel, AbstractProcessedReportModel,
    AbstractWorkerReportCompanyUserModel, AbstractWorkerReportModel, AbstractWorkerReportUserModel,
    AbstractUserModel
    )


class ReportAnswerModel(
    AbstractScheduleTimeSlotModel,
    AbstractCompanyModel,
    AbstractTerritoryModel,
    AbstractProjectModel,
    AbstractProjectTerritoryModel,
    AbstractProjectSchemeModel,
    AbstractGeoPointModel,
    AbstractLevelValueModel,
    AbstractLevelModel,
    AbstractUserModel,
    AbstractWorkerReportCompanyUserModel,
    AbstractWorkerReportModel,
    AbstractWorkerReportUserModel,
    AbstractProcessedReportElementModel,
    AbstractProcessedReportModel,
    ClickhouseModel,
):
    """Модель Answer."""

    key = Column(Nullable(String))
    values = Column(Nullable(String))
    values_qty = Column(Nullable(UInt32))
