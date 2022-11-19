from datetime import datetime
from typing import Optional
from uuid import UUID
from typing_extensions import TypedDict


from pydantic import BaseModel, Field

# Key: day's date
# bottle: 0
# marked: True


class Day(BaseModel):
    id: str = Field(
        title="The date of the day in YYYY-MM-DD format", example='2022-01-31'
    )
    bottles: int = 0
    marked: bool | None = True


# class Month(BaseModel):
#     user_id: Optional[UUID] = None
#     id: str  # 2022-11
#     name: str  # November
#     year: str  # 2022
#     took_bottle_count: 0
#     did_not_take_count: 0
#     days: list[Day]

#     class Config:
#         orm_mode = True

# class Day(BaseModel):
#     id: Optional[UUID] = None
#     name: str
#     active: bool

#     class Config:
#         orm_mode = True


class DayCreate(Day):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
