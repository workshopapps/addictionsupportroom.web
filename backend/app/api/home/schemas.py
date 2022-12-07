from pydantic import BaseModel
import datetime

class NoteCreate(BaseModel):
    title: str
    description: str
    
class Note(BaseModel):
    title: str
    description: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode: True


class ShowNote(Note):
    title: str
    description: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
