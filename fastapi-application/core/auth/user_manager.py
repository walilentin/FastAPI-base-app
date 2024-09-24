from typing import Optional

from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from sqlalchemy.testing.plugin.plugin_base import logging

from core.config import settings
from core.models import User
from core.models.types.user_id import UserIDType

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIDType]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        log.warning(
            "User %r has registered.",
            user.id,
        )

    # async def on_after_forgot_password(
    #     self, user: User, token: str, request: Optional[Request] = None
    # ):
    #     log.warning(
    #         "User %r has forgot their password. Reset token: %r",
    #         user.id,
    #         token,
    #     )
    #
    # async def on_after_request_verify(
    #     self, user: User, token: str, request: Optional[Request] = None
    # ):
    #     log.warning(
    #         "Verification requested for user %r. Verification token: %r",
    #         user.id,
    #         token,
    #     )
