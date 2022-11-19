from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# from db.models.common import TimestampModel, UUIDModel

from db.db import Base
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
