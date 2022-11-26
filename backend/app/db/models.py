from sqlalchemy import Boolean, Column, Integer, String

from db.db import Base

# from db.models.common import TimestampModel, UUIDModel

# from app.db.base_class import Base


'''Example'''


class Example(Base):
    __tablename__ = "example"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    active = Column(Boolean, default=True)


class Day(Base):
    __tablename__ = "days"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    date = Column(String, index=True)
    bottles = Column(Integer, default = 0, index=True)
    marked = Column(Integer, default=True)
# for marked database
# 0 is for False
# 1 is for True

    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="todos")


class Messages(Base):
    """ Table to store contact messages from users"""

    __tablename__ = "messages"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    avatar = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # todos = relationship("Todo", back_populates="owner")

