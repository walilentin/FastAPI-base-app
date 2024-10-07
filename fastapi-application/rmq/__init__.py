from fastapi import APIRouter

from core.config import settings
from .router import router as rmq_router

router = APIRouter(
    prefix=settings.api.v1.message,
    tags=["RabbitMQ"],
)

router.include_router(rmq_router)
