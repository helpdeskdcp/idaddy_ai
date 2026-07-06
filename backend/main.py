from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.core.logger import logger
from backend.core.settings import get_settings
from backend.routes.health import router as health_router
from backend.routes.market import router as market_router
from backend.market.live_service import ws

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting IDaddy AI...")
    ws.start()
    yield
    logger.info("Stopping IDaddy AI...")


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(market_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to IDaddy AI",
        "application": settings.APP_NAME,
        "version": "0.1.0",
    }
