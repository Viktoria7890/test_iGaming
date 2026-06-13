from sqlalchemy.orm import Session

from app.models.payment import Payment


class PaymentRepository:

    def __init__(self, db: Session):
        self.db = db

    def exists(self, clid: str, ts):

        return (
            self.db.query(Payment)
            .filter(
                Payment.clid == clid,
                Payment.ts == ts
            )
            .first()
            is not None
        )

    def save(self, payment: Payment):

        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)

        return payment

    def find_unprocessed(self, clid: str):

        return (
            self.db.query(Payment)
            .filter(
                Payment.clid == clid,
                Payment.processed.is_(False)
            )
            .all()
        )

    def mark_processed(self, payment: Payment):

        payment.processed = True

        self.db.commit()