import app.core.logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import engine
from app.models.base import Base

from app.api.clicks import router as click_router
from app.api.payments import router as payment_router

from app.workers.scheduler import start_scheduler


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):

    start_scheduler()

    yield


app = FastAPI(
    title="Event Processor",
    description="""
Processes Click and Payment events.

Features:
- Click processing
- Payment processing
- Event matching
- Outbox Pattern
- Retry delivery to AdVantage
""",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
def root():
    return {
        "service": "Event Processor",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


app.include_router(click_router)
app.include_router(payment_router)