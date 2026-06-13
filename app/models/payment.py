from datetime import datetime

from sqlalchemy import (
    BigInteger,
    String,
    Float,
    DateTime,
    Boolean,
    UniqueConstraint
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base


class Payment(Base):

    __tablename__ = "payments"

    __table_args__ = (
        UniqueConstraint(
            "clid",
            "ts",
            name="uq_payment_clid_ts"
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    clid: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    payout: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    ts: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    processed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )