from datetime import datetime
from typing import Optional
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    id: int = Field(..., example=1)
    username: str = Field(..., example="name123")
    avatar: str = Field(
        ...,
        example="http://www.example.com/image",
    )
    # chat_status: Optional[str] = Field(..., example=ChatStatus.online)
    # first_name: str = Field(..., example="First name.")
    # last_name: str = Field(..., example="Last Name.")
    # email: EmailStr = Field(..., example="testing@gmail.com")
    # phone_number: Optional[str] = Field(..., example="123456789")
    # bio: Optional[str] = Field(..., example="Your bio goes here.")
    # user_status: str = Field(..., example=UserStatus.active)
    # user_role: Optional[str] = Field(..., example=UserRole.regular)
    # profile_picture: Optional[str] = Field(
    #     ...,
    #     example="{'preview': 'http://www.example.com/image', 'metaData': 'size, type...'}",
    # )

class UserObjectSchema(UserBase):
    pass


class UserCreate(BaseModel):
    username: str = Field(..., example="name123")
    avatar: str = Field(
        ...,
        example="http://www.example.com/image",
    )
    # password: str


class UserOut(UserBase):
    access_token: dict


class ChatStatus(str, Enum):
    online = "online"
    offline = "offline"
    busy = "busy"
    dont_disturb = "don't disturb"


class UserStatus(int, Enum):
    active = 1
    disabled = 0


class UserRole(str, Enum):
    regular = "regular"
    admin = "admin"
