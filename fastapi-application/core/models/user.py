from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from ..mixins.id_int_pm import IdIntMixin


class User(Base, IdIntMixin, SQLAlchemyBaseUserTable[int]):

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyBaseUserTable(session, User)
