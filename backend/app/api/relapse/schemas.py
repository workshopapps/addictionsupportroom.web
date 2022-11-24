from pydantic import BaseModel
from datetime import datetime

class RelapseBase(BaseModel):
    day: datetime

class RelapseModify(RelapseBase):
    day: datetime

