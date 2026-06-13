from datetime import datetime

from sqlalchemy import (
    BigInteger,
    DateTime,
    Integer,
    String,
    JSON
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base

from app.models.outbox_status import OutboxStatus


class Outbox(Base):

    __tablename__ = "outbox"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    payload: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default=OutboxStatus.PENDING
    )

    retry_count: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    next_retry_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )