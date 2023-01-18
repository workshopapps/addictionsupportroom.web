from pydantic import BaseModel
from datetime import datetime
# from typing import 

class ProfileResponseModel(BaseModel):
    username: str
    avater: str | None
    date_added: datetime
    last_relapse_date: datetime | str
    
    class Config():
        orm_mode = True