from pydantic import BaseModel


class Feedback(BaseModel):
    rating: int
    description: str