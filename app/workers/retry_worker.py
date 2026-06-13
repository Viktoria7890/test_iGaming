from datetime import datetime
from datetime import timedelta
import logging

from app.core.database import SessionLocal

from app.repositories.outbox_repository import (
    OutboxRepository
)

from app.services.advantage_service import (
    AdvantageService
)


logger = logging.getLogger(__name__)


class RetryWorker:

    RETRY_DELAYS = [
        1,
        5,
        15,
        30,
        60
    ]

    def run(self):

        db = SessionLocal()

        try:

            repository = OutboxRepository(db)

            advantage_service = (
                AdvantageService()
            )

            pending_events = (
                repository.get_pending()
            )

            for event in pending_events:

                logger.info(
                    f"Processing event {event.id}"
                )

                success = (
                    advantage_service.send(
                        event.payload
                    )
                )

                if success:

                    repository.mark_sent(
                        event
                    )

                    logger.info(
                        f"Event {event.id} marked as SENT"
                    )

                else:

                    retry_index = min(
                        event.retry_count,
                        len(self.RETRY_DELAYS) - 1
                    )

                    delay_minutes = (
                        self.RETRY_DELAYS[
                            retry_index
                        ]
                    )

                    next_retry = (
                        datetime.utcnow()
                        + timedelta(
                            minutes=delay_minutes
                        )
                    )

                    repository.mark_retry(
                        event,
                        next_retry
                    )

                    logger.warning(
                        f"Event {event.id} retry scheduled"
                    )

        finally:
            db.close()