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


class Ranking(BaseModel):
    id: int
    username: str
    avatar: str
    clean_days: int

    class Config:
        orm_mode = True


class TotalCleanDays(BaseModel):
    clean_days: int
    percentage: str
    
    class Config:
        orm_mode = True
        

class SummarySchema(BaseModel):
    milestone: int
    clean_days: int


class RelapseBase(BaseModel):
    day: int = 1
    month: int = 12
    year: int = 2022
    bottles_drank: int = 1


class RelapseCreate(RelapseBase):
    pass


class RelapseInDBBase(RelapseBase):
    day: int
    month: int
    year: int
    bottles_drank: int
    user: int

    class config:
        orm_mode = True


class RelapseInDB(RelapseInDBBase):
    pass


class StreakBase(BaseModel):
    pass


class StreakInDBBase(StreakBase):
    start_date: int
    current_date: int
    last_relapse: int
    user: int

    class config:
        orm_mode = True


class StreakInDB(StreakInDBBase):
    pass


class Months(BaseModel):
    title: str
    bottle_count: int

    class Config:
        orm_mode = True


class GetAllHistoryResult(BaseModel):
    status_code: int
    result: list[Months]


class GetAllRanking(BaseModel):
    status_code: int
    result: list[Ranking]
