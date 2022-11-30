from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.utils.mixins import Base
from .schemas import RelapseCreate
from db.models import Relapse
from datetime import datetime

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, model_id: Any) -> Optional[ModelType]:
        return db.query(self.model).get(model_id)

    def get_multi(self,
                  db: Session,
                  *,
                  skip: int = 0,
                  limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: ModelType,
               obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, model_id: int) -> ModelType:
        obj = db.query(self.model).get(model_id)
        db.delete(obj)
        db.commit()
        return obj


class CRUDRelapse(CRUDBase[Relapse, RelapseCreate, RelapseCreate]):
    """
    Relapse CRUD
    """

    def create_with_user(self, db: Session, *, obj_in: RelapseCreate,
                         user_id: int, month_id: int) -> Relapse:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Relapse(day=obj_in.day,
                         month=obj_in.month,
                         year=obj_in.year,
                         bottles_drank=obj_in.bottles_drank,
                         user=user_id,
                         month_id=month_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_user(self,
                          db: Session,
                          *,
                          user_id: int,
                          skip: int = 0,
                          limit: int = 100) -> List[Relapse]:
        return (db.query(Relapse).filter(
            Relapse.user == user_id).offset(skip).limit(limit).all())


def create_relapse_with_user(db: Session, user_id: int,
                             relapse: RelapseCreate):
    db_relapse = Relapse(day=relapse.day,
                         month=relapse.month,
                         year=relapse.year,
                         user=user_id)
    db.add(db_relapse)
    db.commit()
    db.refresh(db_relapse)
    return db_relapse


relapse = CRUDRelapse(Relapse)
