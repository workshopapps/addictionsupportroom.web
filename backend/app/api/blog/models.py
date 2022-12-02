from api.utils.mixins import Base
from sqlalchemy import String, Integer, Column, DateTime, Boolean
import datetime

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    sober_tip = Column(Boolean)
    story = Column(Boolean)
    family = Column(Boolean)
    article = Column(Boolean)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())