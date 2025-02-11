from app.models.clickhouse.abstract import ClickhouseModel,  AbstractLevelModel


class LevelModel(AbstractLevelModel, ClickhouseModel):
    """Модель Level."""
