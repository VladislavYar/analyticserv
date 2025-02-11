from app.models.clickhouse.abstract import ClickhouseModel,  AbstractLevelValueModel


class LevelValueModel(AbstractLevelValueModel, ClickhouseModel):
    """Модель LevelValue."""
