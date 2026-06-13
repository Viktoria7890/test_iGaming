from datetime import datetime

from sqlalchemy import (
    BigInteger,
    String,
    Integer,
    Float,
    DateTime
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base


class Click(Base):

    __tablename__ = "clicks"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    clid: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    ad_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    click_spend: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    ts: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )