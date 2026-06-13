from datetime import datetime

from sqlalchemy.orm import Session

from app.models.outbox import Outbox


class OutboxRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, payload):

        event = Outbox(
            payload=payload
        )

        self.db.add(event)

        self.db.commit()

        self.db.refresh(event)

        return event

    def get_pending(self):

        return (
            self.db.query(Outbox)
            .filter(
                Outbox.status == "PENDING",
                Outbox.next_retry_at <= datetime.utcnow()
            )
            .all()
        )

    def mark_sent(
        self,
        event
    ):
        event.status = "SENT"
        self.db.commit()

    def mark_retry(
        self,
        event,
        next_retry
    ):
        event.retry_count += 1
        event.next_retry_at = next_retry

        self.db.commit()