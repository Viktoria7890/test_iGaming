from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dto.click import ClickDTO

from app.repositories.click_repository import (
    ClickRepository
)

from app.repositories.payment_repository import (
    PaymentRepository
)

from app.repositories.outbox_repository import (
    OutboxRepository
)

from app.services.click_service import (
    ClickService
)

from app.services.matching_service import (
    MatchingService
)

router = APIRouter()


@router.post("/click")
def create_click(
    dto: ClickDTO,
    db: Session = Depends(get_db)
):

    click_repository = ClickRepository(db)

    payment_repository = PaymentRepository(db)

    outbox_repository = OutboxRepository(db)

    click_service = ClickService(
        click_repository
    )

    matching_service = MatchingService(
        click_repository,
        payment_repository,
        outbox_repository
    )

    click = click_service.create_click(
        dto.clid,
        dto.ad_id,
        dto.click_spend,
        dto.ts
    )

    matching_service.try_match(
        dto.clid
    )

    return {
        "status": "accepted"
    }