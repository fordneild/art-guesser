from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Object


class BaseService:
    def __init__(self, db: Session) -> None:
        self.db = db


class ObjectService(BaseService):
    def list(self):
        a = self.db.query(Object).limit(5).all()
        return a
