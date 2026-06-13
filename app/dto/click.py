from datetime import datetime

from pydantic import BaseModel


class ClickDTO(BaseModel):
    clid: str
    ad_id: int
    click_spend: float
    ts: datetime