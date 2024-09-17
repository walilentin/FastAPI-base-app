from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column


class IdIntMixin:

    id: Mapped[int] = mapped_column(primary_key=True)