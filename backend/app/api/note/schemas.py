from pydantic import BaseModel




class Note(BaseModel):
    title: str
    description: str
     
    class Config:
        orm_mode: True