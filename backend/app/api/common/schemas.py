from pydantic import BaseModel, Field
from typing import (
    Any,
)


class ResponseSchema(BaseModel):
    """
    A Pydantic class that defines a Response schema object.

    Args:
        status_code (int) : Response status code.
        message (str) : Response message.

    Example:
        >>> status_code = 200
        >>> message = "You have logged in successfully!"
    """

    status_code: int = Field(
        ...,
        example=400,
    )
    message: str = Field(
        ...,
        example="A message to indicate that the request was not successful!",
    )
    data: Any | None = Field(
        example="Data !",
    )
