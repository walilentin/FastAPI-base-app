from core.config import settings
from .users import router as user_router
from fastapi import APIRouter

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(
    user_router,
    prefix=settings.api.v1.users,
)