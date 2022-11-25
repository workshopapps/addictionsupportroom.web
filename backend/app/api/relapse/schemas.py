from pydantic import BaseModel

class RelapseBase(BaseModel):
    day: int
    month: int
    year: int

class RelapseCreate(RelapseBase):
    pass

class RelapseInDBBase(RelapseBase):
    day: int
    month: int
    year: int
    user: int

    class config:
        orm_mode = True

class RelapseInDB(RelapseInDBBase):
    pass