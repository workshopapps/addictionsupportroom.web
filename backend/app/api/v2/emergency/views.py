from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import deps
from db.models import Emergency
from .crud import find_user, new_emergency

router = APIRouter()

class EmergencyRequest(BaseModel):
    username: str
    relapse: bool


@router.post("/add")
def add_emergency(data:EmergencyRequest, db: Session = Depends(deps.get_db)):
    if data.relapse == True:

        user = find_user("lion", db)

        new_emergency(user["id"], user["username"], user["avatar"], db)

        return {
            "success": True,
            "message": "Someone will reach out soon."
        }


@router.get("/all")
def all_emergencies(db: Session = Depends(deps.get_db)):
    all_emergencies = db.query(Emergency).all()
    return all_emergencies
