from sqlalchemy import Column, String, Integer, DateTime 
from db.db import Base
import datetime


class Rank(Base):
    __tablename__ = "ranks"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    avatar = Column(String)
    start_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    current_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    clean_days = Column(String, default="0")
    # user = Column(ForeignKey('users.id'), index=True)