import uuid
from datetime import datetime

from sqlalchemy import UUID, String, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from api.database.base import Base


class Chip(Base):
    __tablename__ = "chip"

    id: Mapped[uuid.uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'), unique=True, nullable=True)
    pairing_token: Mapped[str] = mapped_column(String(8), unique=True, nullable=False)
    sn: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
