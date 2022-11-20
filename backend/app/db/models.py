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

    id = Column(Integer, primary_key=True, index=True)
    bottles = Column(Integer)
    marked = Column(Boolean, default=True)

    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="todos")


class Messages(Base):
    """ Table to store contact messages from users"""
    
    __tablename__ = "messages"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String, nullable=False)
    message = Column(String, nullable=False)

class Quote(Base):
    """ Table for storing quotes"""

    __tablename__ = "quotes"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    mood = Column(String, nullable=False)
    quote = Column(String, nullable=False)

