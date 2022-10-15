from pydantic import BaseModel


class ObjectDomain(BaseModel):
    title: str

    class Config:
        orm_mode = True
