from fastapi_users import FastAPIUsers

from api.dependencies.auth.backend import authentication_backend
from api.dependencies.auth.user_manager import get_user_manager
from core.models import User
from core.models.types.user_id import UserIDType

fastapi_users = FastAPIUsers[User, UserIDType](
    get_user_manager,
    [authentication_backend],
)

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
