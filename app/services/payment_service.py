from app.models.payment import Payment

from app.repositories.payment_repository import (
    PaymentRepository
)


class PaymentService:

    def __init__(
        self,
        payment_repository: PaymentRepository
    ):
        self.payment_repository = payment_repository

    def create_payment(
        self,
        clid,
        payout,
        ts
    ):

        if self.payment_repository.exists(
            clid,
            ts
        ):
            return None

        payment = Payment(
            clid=clid,
            payout=payout,
            ts=ts
        )

        return self.payment_repository.save(
            payment
        )