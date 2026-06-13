from sqlalchemy.orm import Session

from app.models.click import Click


class ClickRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_clid(self, clid: str):
        return (
            self.db.query(Click)
            .filter(Click.clid == clid)
            .first()
        )

    def exists(self, clid: str) -> bool:
        return self.get_by_clid(clid) is not None

    def save(self, click: Click):

        self.db.add(click)
        self.db.commit()
        self.db.refresh(click)

        return click