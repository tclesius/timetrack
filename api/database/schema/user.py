import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import mapped_column, Mapped

from api.database.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[uuid.uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rfid_token: Mapped[str] = mapped_column(String(8), unique=True, nullable=True)
    first_name: Mapped[str] = mapped_column(String(20))
    last_name: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(128))
