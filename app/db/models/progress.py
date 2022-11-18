from sqlalchemy import ForeignKey, Integer
from db.models.common import TimestampModel, UUIDModel


class Progress(TimestampModel, UUIDModel, table=True):
    __tablename__ = "example"

    name: str
    active: bool = True

    def __repr__(self):
        return f"<Example (id: {self.id})>"


class Day(TimestampModel, UUIDModel, table=True):
    __tablename__ = "example"

    name: str
    active: bool = True

    def __repr__(self):
        return f"<Example (id: {self.id})>"
    

class Day(TimestampModel):
    __tablename__ = "days"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="todos")
