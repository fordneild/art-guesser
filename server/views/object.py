from typing import List
from domain import ObjectDomain
from service import ObjectService
from pydantic import BaseModel
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from views.base import BaseView

router = InferringRouter()


class ObjectId(BaseModel):
    id: int


class TitleReponse(BaseModel):
    title: str


class YearReponse(BaseModel):
    year: int


@cbv(router)
class ObjectView(BaseView):
    @property
    def service(self):
        return ObjectService(self.db)

    @router.get("/objects", response_model=List[ObjectDomain])
    async def list_objects(self):
        return self.service.list()

    @router.post("/year", response_model=YearReponse)
    async def get_year_by_id(self, object_payload: ObjectId):
        year = self.service.get_year_by_id(object_id=object_payload.id)
        return YearReponse(year=year)

    @router.post("/title", response_model=List[TitleReponse])
    async def get_title_by_year(self, object_year: YearReponse):
        titles = self.service.get_title_by_year(year=object_year.year)
        return [TitleReponse(title=t) for t in titles]
