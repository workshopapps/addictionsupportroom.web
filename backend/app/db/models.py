from sqlalchemy import Boolean, Column, Integer, String

# from db.db import Base

from enum import Enum
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)

# from db.models.common import TimestampModel, UUIDModel

# from app.db.base_class import Base

from api.utils.mixins import (
    Base,
    CommonMixin,
    TimestampMixin,
)

"""Example"""


class Example(Base):
    __tablename__ = "example"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    active = Column(Boolean, default=True)


class Day(Base):
    __tablename__ = "days"

    day_id = Column(String, primary_key=True, index=True)
    bottles = Column(Integer, default=0)
    marked = Column(Boolean, default=True)

    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="todos")


class ContactusMessages(Base):
    """Table to store contact messages from users"""

    __tablename__ = "contact_us_messages"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    message = Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    avatar = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # todos = relationship("Todo", back_populates="owner")


class MessageStatus(int, Enum):
    """
    Enum class to define a message status.

    Args:
        READ (int) : A constant integer to indicate that the recipient read the message.
        NOT_READ (int) : A constant integer to indicate that the recipient didn't read the message.
    """

    READ = 0
    NOT_READ = 1


class Messages(Base, CommonMixin, TimestampMixin):  # pylint: disable=R0903
    """
    The `messages` model.

    Args:
        __table_args__ (dict) : SqlAlchemy configs to convert from COLUMNAR to ROWSTORE.
        sender (int) : A user id foreign key value for the sender of the message.
        receiver (int) : A user id foreign key value for the recipient of the message.
        room (int) : A room id foreign key value of the message.
        content (str) : The content of the message.
        status (int) : The status of the message(e.g. read or not read).
        message_type (str) : The message type(e.g. 'text' or 'media').
        media (str) : A relative URL to the location of the image on the Deta drive.
    """

    # __table_args__ = {
    #     "mysql_engine": "InnoDB",
    #     "prefixes": ["ROWSTORE", "REFERENCE"],
    # }

    sender: int = Column(ForeignKey("users.id"), index=True)
    receiver: int = Column(ForeignKey("users.id"), index=True)
    room: int = Column(ForeignKey("rooms.id"), index=True, default=None)
    content: str = Column(String(1024), index=True)
    status: int = Column(Integer, index=True, default=MessageStatus.NOT_READ.value)
    message_type: str = Column(String(10), index=True)
    media: str | None = Column(String(220), nullable=True)


class UserStatus(int, Enum):
    banned = 1
    not_banned = 0


class UserRole(int, Enum):
    admin = 1
    not_admin = 0


class Rooms(Base, CommonMixin, TimestampMixin):
    # __table_args__ = {
    #     "mysql_engine": "InnoDB",
    #     "prefixes": ["ROWSTORE", "REFERENCE"],
    # }

    room_name: int = Column(String(20), index=True)
    description: str = Column(String(60))


class RoomMembers(Base, CommonMixin, TimestampMixin):
    # __table_args__ = {
    #     "mysql_engine": "InnoDB",
    #     "prefixes": ["ROWSTORE", "REFERENCE"],
    # }

    room: int = Column(ForeignKey("rooms.id"), index=True)
    member: int = Column(ForeignKey("users.id"), index=True)
    banned: UserStatus | None = Column(Integer, index=True)
    admin: UserRole | None = Column(Integer, index=True)
