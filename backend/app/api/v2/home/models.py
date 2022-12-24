from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime

from ...mixins import (
    Base,
    CommonMixin,
    TimestampMixin,
)
from sqlalchemy.orm import relationship

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='notes')
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime,
                        default=datetime.date(datetime.today()),
                        nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.date(datetime.today()),
                        nullable=False)

class LeadCollected(Base):
    __tablename__ = 'lead_collected_email'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
