from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import deps
from db.models import Emergency, User
from datetime import datetime


router = APIRouter()


class NewEmergency(BaseModel):
    username: str


@router.get("/")
def all_emergencies():
    #return a list of all existing emergencies
    emergencies = list(Emergency.query.all())

    return emergencies



@router.post("/")
def new_emergency(data: NewEmergency, db: Session = Depends(deps.get_db)):

    # Get the username from data
    try:
        name = data.username
    except:
        return {"error": "No username found in request"}
    
    # Get the existing username from the database
    try:
        user = User.query.get(name)
    except:
        return {"error": "Wrong username"}
    
    #Add the user to the emergency database
    try:
        add_emergency = Emergency(name=user.name, avatar=user.avatar, created_at=datetime.utcnow())
        db.add(add_emergency)
        db.commit()
    except:
        return {"error": "internal server error. try again later."}
    
    return {"success": "keep calm. someone will reach out soon."}

