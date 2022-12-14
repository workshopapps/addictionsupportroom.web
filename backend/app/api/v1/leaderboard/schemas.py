from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field



class Ranking(BaseModel):
    id: int
    username: str
    avatar: str
    start_date: datetime
    current_date: datetime
    clean_days: str
    
    class Config:
        orm_mode = True 