from app.models.clickhouse.abstract import (
    ClickhouseModel, AbstractScheduleTimeSlotModel, AbstractCompanyModel,
    AbstractTerritoryModel, AbstractProjectTerritoryModel, AbstractProjectSchemeModel,
    AbstractGeoPointModel, AbstractLevelModel, AbstractLevelValueModel, AbstractProjectModel,
    )


class ScheduleTimeSlotModel(
    AbstractScheduleTimeSlotModel,
    AbstractCompanyModel,
    AbstractTerritoryModel,
    AbstractProjectModel,
    AbstractProjectTerritoryModel,
    AbstractProjectSchemeModel,
    AbstractGeoPointModel,
    AbstractLevelValueModel,
    AbstractLevelModel,
    ClickhouseModel,
):
    """Модель ScheduleTimeSlot."""
