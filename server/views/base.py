from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from fastapi import Depends

from database import SessionLocal


# Dependency
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class BaseView(ABC):
    db: Session = Depends(get_db)

    @property
    @abstractmethod
    def service(self):
        pass
