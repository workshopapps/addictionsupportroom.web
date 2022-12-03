from pydantic import BaseModel
import datetime


class BlogSchema(BaseModel):
    title: str
    body: str
    sober_tip: bool = False
    story: bool = False
    family: bool = False
    article: bool = False
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True 
