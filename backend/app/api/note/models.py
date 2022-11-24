from sqlalchemy import Column, String, Integer, DateTime 
from db.db import Base
from datetime import datetime


class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.date(datetime.today()), nullable=False)
    updated_at = Column(DateTime, default=datetime.date(datetime.today()), nullable=False)
    