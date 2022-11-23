from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Examples(BaseModel):
    id: str | None
    name: str
    active: bool

    class Config:
        orm_mode = True


class ExampleSchema(Examples):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True)
#     avatar = Column(String)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)


class UserBase(BaseModel):
    username: str
    avatar: str


class UserCreate(UserBase):
    pass
    # password: str


class UserOut(UserBase):
    access_token: dict
