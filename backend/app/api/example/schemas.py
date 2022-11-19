from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class DayCreate(BaseModel):
    id: Optional[UUID] = None
    name: str
    active: bool

    class Config:
        orm_mode = True


class ExampleSchema(DayCreate):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
