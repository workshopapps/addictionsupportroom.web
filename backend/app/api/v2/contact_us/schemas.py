from pydantic import BaseModel, Field


class Contact(BaseModel):
    username: str
    message: str

class NewsLetterEmail(BaseModel):
    email: str = Field(default="contactUs@app.soberpal.com")
