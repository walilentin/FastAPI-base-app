from typing import Annotated

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from api.dependencies.auth.users import get_users_db
from core.auth.user_manager import UserManager


async def get_user_manager(
    user_db: Annotated["SQLAlchemyUserDatabase", Depends(get_users_db)]
):
    yield UserManager(user_db)
