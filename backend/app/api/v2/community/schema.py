from pydantic import BaseModel
import datetime

class EmergencyResponseModel(BaseModel):
    name: str
    avatar: str
    created_at: datetime.datetime

    class Config():
        orm_mode = True
