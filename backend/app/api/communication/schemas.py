import datetime

from pydantic import (
    BaseModel,
    Field,
)
from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from api.auth.schemas import UserObjectSchema

class MessageCreate(BaseModel):
    """
    A Pydantic class that defines the message response schema for sending messages.

    Args:
        receiver (user_id) : The id of the message's recipient.
        content (str) : The content of the message.
        message_type (str) : The type of the message(e.g. 'text' or 'media').
        media (str) : A relative URL to the Deta drive.

    Example:
        >>> receiver = "4"
        >>> content = "Hello there!"
        >>> message_type = "text"
        >>> media = ""
    """

    receiver: str = Field(..., example="The recipient id for this message.")
    content: str = Field(..., example="The message text content.")
    message_type: str = Field(..., example="Message type(e.g. 'text' or 'media')")
    media: Optional[str] = Field(
        ...,
        example="A relative URL to the Deta drive.",
    )


class MessageCreateRoom(BaseModel):
    """
    A Pydantic class that defines the message response schema for sending messages in a room.

    Args:
        room (str) : A room name.
        content (str) : The content of the message.
        message_type (str) : The type of the message(e.g. 'text' or 'media').
        media (str) : A relative URL to the Deta drive.

    Example:
        >>> room = "nerds"
        >>> content = "Hello there!"
        >>> message_type = "text"
        >>> media = ""
    """

    room: str = Field(..., example="A unique room name(e.g. 'nerds'). Case Sensitive.")
    content: str = Field(..., example="The message text content.")
    message_type: str = Field(..., example="Message type(e.g. 'text' or 'media')")
    media: Optional[str] = Field(
        ..., example="A dictionary that contains media url, type..."
    )


class GetAllMessageResults(BaseModel):
    """
    A Pydantic class that defines the message response schema for fetching all messages.

    Args:
        status_code (int) : A response status code.
        result (List[Dict[str, Any]]) : A secure password.
    """

    status_code: int = Field(..., example=200)
    result: List[Dict[str, Any]]

class DeleteChatMessages(BaseModel):
    """
    A Pydantic class that defines the message response schema for deleting messages.

    Args:
        contact (user_id) : The recipient id for the sent messages to be deleted.
    """

    contact: str = Field(
        ...,
        example="The recipient id for the sent messages to be deleted.",
    )


class RoomCreate(BaseModel):
    join: int
    room_name: str
    description: str


class RoomCreateResult(BaseModel):
    room_name: str
    members: list[str]
    conversation: list[str]
    active: str
    creation_date: datetime.datetime


class RoomGetALL(BaseModel):
    room_name: str
    members: list[dict[str, str | datetime.datetime]]
    messages: list[dict[str, str | datetime.datetime]]
    active: str
    creation_date: datetime.datetime

class GetAllContactsResults(BaseModel):
    status_code: int
    result: list[UserObjectSchema]
