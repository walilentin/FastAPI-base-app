from fastapi import APIRouter

from api.dependencies.auth.f_users import fastapi_users
from core.config import settings
from core.schemas.user import UserUpdate, UserRead

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)
# /me
router.include_router(
    router=fastapi_users.get_users_router(UserRead, UserUpdate),
)
