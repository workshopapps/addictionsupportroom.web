from sqlalchemy import Boolean, Column, Integer, String, DateTime, Date
import datetime
# from db.db import Base
import datetime
from enum import Enum
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)

# from db.models.common import TimestampModel, UUIDModel

# from app.db.base_class import Base

from api.mixins import (
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


class ContactusMessages(Base):
    """Table to store contact messages from users"""

    __tablename__ = "contact_us_messages"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    message = Column(String, nullable=False)


class ForumPost(Base):
    __tablename__ = 'forum_post'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    date_posted = Column(DateTime,
                         default=datetime.datetime.utcnow,
                         nullable=False)
    user_username = Column(String, ForeignKey('users.username'))
    user = relationship('User', back_populates='forum_posts')
    forum_post_comments = relationship('ForumPostComment',
                                       back_populates='origin_post')


class ForumPostComment(Base):
    __tablename__ = 'forum_post_comments'
    id = Column(Integer, primary_key=True, index=True)
    owner_username = Column(String, ForeignKey('users.username'))
    owner = relationship('User', back_populates='forum_comments')
    origin_post_id = Column(Integer, ForeignKey('forum_post.id'))
    origin_post = relationship('ForumPost',
                               back_populates='forum_post_comments')
    comment = Column(String)
    date_posted = Column(DateTime,
                         default=datetime.datetime.utcnow,
                         nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    avatar = Column(String, nullable=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    forum_posts = relationship('ForumPost', back_populates='user')
    forum_comments = relationship('ForumPostComment', back_populates='owner')
    date_added = Column(DateTime,
                        default=datetime.datetime.utcnow,
                        nullable=False)
    last_relapse_date = Column(
        Date,
        nullable=False,
        default=datetime.date.today(),
        # default=datetime.date(2008, 11, 25),
    )


class Month(Base):
    __tablename__ = "months"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(ForeignKey('users.id'), index=True)
    title = Column(String)
    relapses = relationship("Relapse", back_populates="month_history")


class Relapse(Base):
    __tablename__ = "relapses"
    id = Column(Integer, primary_key=True, index=True)
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    bottles_drank = Column(Integer, nullable=False)
    user = Column(ForeignKey('users.id'), index=True)
    month_id = Column(ForeignKey('months.id'))
    month_history = relationship("Month", back_populates="relapses")


class Streak(Base):
    __tablename__ = "streaks"
    id = Column(Integer, primary_key=True, index=True)

    user = Column(ForeignKey('users.id'), index=True)


class MessageState(int, Enum):
    """
    Enum class to define a message state.

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
        state (int) : The status of the message(e.g. read or not read).
        status (int) : The status of the message(e.g. sent or not recieved).
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
    status: str = Column(String(1024), index=True)
    state: int = Column(Integer,
                        index=True,
                        default=MessageState.NOT_READ.value)
    message_type: str = Column(String(20), index=True)
    # media: str | None = Column(String(220), nullable=True)
    # preview


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


class Emergency(Base):

    __tablename__ = "emergencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    avatar = Column(String)
    created_at = Column(DateTime)


class NewsLetterEmail(Base):
    __tablename__ = 'news_letter_email'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    sober_tip = Column(Boolean)
    story = Column(Boolean)
    family = Column(Boolean)
    article = Column(Boolean)
    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.datetime.utcnow())
    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.datetime.utcnow())


class Feedbacks(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    description = Column(String)
    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, nullable=True)


class Note(Base):
    __tablename__ = "notes"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=True)
    description = Column(String)
    created_at = Column(DateTime,
                        default=datetime.datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.datetime.utcnow(),
                        nullable=False)

class LeadCollected(Base):
    __tablename__ = 'lead_collected_email'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)