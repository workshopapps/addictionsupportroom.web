from typing import str
from pydantic import BaseModel

class RelapseBase(BaseModel):
    day: str

class RelapseModify(RelapseBase):
    day: str

