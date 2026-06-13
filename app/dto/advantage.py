from datetime import datetime

from pydantic import BaseModel


class AdvantageDTO(BaseModel):

    clid: str

    payout: float

    click_spend: float

    click_ts: datetime

    payment_ts: datetime

    payout_currency: str = "USD"

    click_spend_currency: str = "USD"