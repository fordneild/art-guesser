from typing import List
from domain import ObjectDomain
from service import ObjectService
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from views.base import BaseView

router = InferringRouter()  # Step 1: Create a router


@cbv(router)
class ObjectView(BaseView):
    @property
    def service(self):
        return ObjectService(self.db)

    @router.get("/objects", response_model=List[ObjectDomain])
    async def list_objects(self):
        return self.service.list()
