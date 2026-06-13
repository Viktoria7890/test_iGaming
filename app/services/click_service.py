from app.models.click import Click
from app.repositories.click_repository import ClickRepository


class ClickService:

    def __init__(
        self,
        click_repository: ClickRepository
    ):
        self.click_repository = click_repository

    def create_click(
            self,
            clid,
            ad_id,
            click_spend,
            ts
    ):
        print("CHECKING:", clid)

        if self.click_repository.exists(clid):
            print("CLICK ALREADY EXISTS")
            return None

        print("CREATING CLICK")

        click = Click(
            clid=clid,
            ad_id=ad_id,
            click_spend=click_spend,
            ts=ts
        )

        return self.click_repository.save(click)