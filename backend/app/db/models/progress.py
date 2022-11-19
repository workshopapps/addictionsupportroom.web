from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.db import Base

from db.models.common import TimestampModel, UUIDModel


# class Progress(TimestampModel, UUIDModel, table=True):
#     __tablename__ = "example"

#     name: str
#     active: bool = True

#     def __repr__(self):
#         return f"<Example (id: {self.id})>"


# class Day(BaseModel):
#     id: str = Field(
#         title="The date of the day in YYYY-MM-DD format", example='2022-01-31'
#     )
#     bottles: int = 0
#     marked: bool | None = True


class Day(Base):
    __tablename__ = "days"

    id = Column(Integer, primary_key=True, index=True)
    bottles = Column(Integer)
    marked = Column(Boolean, default=True)

    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="todos")

# class Day(TimestampModel, table=True, primary_key=True):
#     __tablename__ = "days"

#     id: str
#     bottles: int = 0
#     marked: bool = True

#     def __repr__(self):
#         return f"<Day (id: {self.id})>"
