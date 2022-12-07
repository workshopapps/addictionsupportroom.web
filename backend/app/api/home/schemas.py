from pydantic import BaseModel
import datetime
from typing import Any

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

class Emotion(BaseModel):
    emotion: str

class ResponseModel(BaseModel):
    """Creates a response model for the Quote endpoint.

    Provides a structure for providing a response to the request.

    Provides a static method for success responses

    Attributes:
        status: The status of the response.
        message: The message of the response.
        data: The data of the response.
    """

    status: str
    message: str
    data: Any