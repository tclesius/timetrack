import datetime
import enum
import uuid

from sqlalchemy import UUID, DateTime, ForeignKey, Enum
from sqlalchemy.orm import mapped_column, Mapped

from api.database.base import Base


class DeviceType(enum.Enum):
    hardware = 1
    web = 2


class Log(Base):
    __tablename__ = "log"

    id: Mapped[uuid.uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("user.id"))
    start_timestamp: Mapped[datetime.datetime] = mapped_column(DateTime)
    end_timestamp: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    device: Mapped[int] = mapped_column(Enum(DeviceType), nullable=True)
