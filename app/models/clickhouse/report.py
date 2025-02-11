from app.models.clickhouse.abstract import (
    ClickhouseModel, AbstractScheduleTimeSlotModel, AbstractCompanyModel,
    AbstractTerritoryModel, AbstractProjectTerritoryModel, AbstractProjectSchemeModel,
    AbstractGeoPointModel, AbstractLevelModel, AbstractLevelValueModel, AbstractProjectModel,
    AbstractProcessedReportElementModel, AbstractProcessedReportModel,
    AbstractWorkerReportCompanyUserModel, AbstractWorkerReportModel, AbstractWorkerReportUserModel,
    AbstractUserModel
    )


class ReportModel(
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
    """Модель Report."""
