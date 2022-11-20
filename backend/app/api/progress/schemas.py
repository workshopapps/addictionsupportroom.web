from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Examples(BaseModel):
    id: str | None
    name: str
    active: bool

    class Config:
        orm_mode = True


class ExampleSchema(Examples):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class Day(BaseModel):
    day_id: str | None = Field(
        title="The date of the day in YYYY-MM-DD format", example='2022-01-31'
    )
    bottles: int
    marked: bool | None = True

    class Config:
        orm_mode = True
