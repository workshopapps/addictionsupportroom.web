from pydantic import BaseModel
from datetime import datetime




class Note(BaseModel):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
     
    class Config:
        orm_mode: True
        
        
class ShowNote(Note):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
    