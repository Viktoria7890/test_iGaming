from app.dto.advantage import AdvantageDTO


class MatchingService:

    def __init__(
        self,
        click_repository,
        payment_repository,
        outbox_repository
    ):
        self.click_repository = click_repository

        self.payment_repository = payment_repository

        self.outbox_repository = outbox_repository

    def try_match(self, clid: str):

        click = self.click_repository.get_by_clid(
            clid
        )

        if not click:
            return

        payments = (
            self.payment_repository
            .find_unprocessed(clid)
        )

        for payment in payments:

            event = AdvantageDTO(
                clid=clid,
                payout=payment.payout,
                click_spend=click.click_spend,
                click_ts=click.ts,
                payment_ts=payment.ts
            )

            self.outbox_repository.save(
                event.model_dump(
                    mode="json"
                )
            )

            self.payment_repository.mark_processed(
                payment
            )