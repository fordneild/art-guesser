from typing import Dict, List
from pydantic import BaseModel


class ObjectImage(BaseModel):
    src: str
    width: int
    height: int


class ObjectDomain(BaseModel):
    id: int
    title: str
    terms: List[Dict[str, str]]
    image: ObjectImage
