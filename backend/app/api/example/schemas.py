from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Examples(BaseModel):
    id: str | None
    name: str
    active: bool

    class Config:
        orm_mode = True


class ExampleSchema(Examples):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
