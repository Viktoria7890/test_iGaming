from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dto.payment import PaymentDTO

from app.repositories.click_repository import (
    ClickRepository
)

from app.repositories.payment_repository import (
    PaymentRepository
)

from app.repositories.outbox_repository import (
    OutboxRepository
)

from app.services.payment_service import (
    PaymentService
)

from app.services.matching_service import (
    MatchingService
)

router = APIRouter()


@router.post("/payment")
def create_payment(
    dto: PaymentDTO,
    db: Session = Depends(get_db)
):

    click_repository = ClickRepository(db)

    payment_repository = PaymentRepository(db)

    outbox_repository = OutboxRepository(db)

    payment_service = PaymentService(
        payment_repository
    )

    matching_service = MatchingService(
        click_repository,
        payment_repository,
        outbox_repository
    )

    payment_service.create_payment(
        dto.clid,
        dto.payout,
        dto.ts
    )

    matching_service.try_match(
        dto.clid
    )

    return {
        "status": "accepted"
    }