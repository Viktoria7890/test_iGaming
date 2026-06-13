from datetime import datetime

from pydantic import BaseModel


class PaymentDTO(BaseModel):
    clid: str
    payout: float
    ts: datetime