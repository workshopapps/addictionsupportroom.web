from pydantic import BaseModel

class RelapseBase(BaseModel):
    day: int
    month: int
    year: int
    bottles_drank: int

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
