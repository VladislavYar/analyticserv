from typing import AsyncGenerator
import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from app.kafka.analytic_consumer import AnalyticConsumer
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Запускает consumer Kafka.

    Args:
        app (FastAPI): объект сервиса.

    Returns:
        AsyncGenerator[None, None]: None.
    """
    asyncio.create_task(AnalyticConsumer().start())
    yield


app_data = settings.app_settings

app = FastAPI(title=app_data.serive_name, lifespan=lifespan)

if __name__ == '__main__':
    uvicorn.run(
        app=app_data.asgi_app_path,
        host=app_data.asgi_host,
        port=app_data.asgi_port,
        reload=app_data.asgi_reload,
        )
