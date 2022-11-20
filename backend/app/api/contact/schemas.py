from pydantic import BaseModel


class Contact(BaseModel):
    username: str
    message: str