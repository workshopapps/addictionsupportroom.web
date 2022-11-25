from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.models import Example, Base
from db.database import engine
from fastapi import APIRouter, Depends

from api import deps
from db.models import User
from db.database import get_db
from datetime import datetime

router = APIRouter()


class NewEmergency(BaseModel):
    username: str


@router.get("/emergencies")
def all_emergencies(db: Session = Depends(get_db)):
    #return a list of all existing emergencies
    emergencies = db.query(User).all()

    return emergencies
