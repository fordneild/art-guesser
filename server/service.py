from typing import Optional
from sqlalchemy.orm import Session

from models import Object, ObjectsTerm, PublishedImage
from sqlalchemy import func

from domain import ObjectDomain, ObjectImage


class BaseService:
    def __init__(self, db: Session) -> None:
        self.db = db


class ObjectService(BaseService):
    classifications = ("Painting", "Drawing")

    def format_image_src(self, src: str, width: int, height: int) -> str:
        return f"{src}/full/!{width},{height}/0/default.jpg"

    def list(self, limit: Optional[int] = 5):
        terms_agg = func.array_agg(
            func.json_build_object(ObjectsTerm.termtype, ObjectsTerm.term),
        ).label("terms")
        objects_with_terms = (
            self.db.query(
                Object.objectid,
                Object.title,
                terms_agg,
            )
            .filter(Object.classification.in_(self.classifications))
            .join(
                ObjectsTerm,
                ObjectsTerm.objectid == Object.objectid,
            )
            .group_by(Object.objectid)
            .subquery()
        )
        objects = (
            self.db.query(
                objects_with_terms,
                PublishedImage.iiifurl,
                PublishedImage.width,
                PublishedImage.height,
            )
            .join(
                PublishedImage,
                PublishedImage.depictstmsobjectid == objects_with_terms.c.objectid,
            )
            .order_by(func.random())
            .limit(limit)
            .all()
        )

        return [
            ObjectDomain(
                id=objectid,
                title=title,
                terms=terms,
                image=ObjectImage(
                    src=self.format_image_src(
                        img_src, width=img_width, height=img_height
                    ),
                    width=img_width,
                    height=img_height,
                ),
            )
            for objectid, title, terms, img_src, img_width, img_height in objects
        ]
