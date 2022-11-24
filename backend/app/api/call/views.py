from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import deps
from db.models import User
from .agora import Agora


router = APIRouter()


class Call(BaseModel):
    id: int


@router.post("/")
def joinCall(data: Call, db: Session = Depends(deps.get_db)):
    #returns an agora token for joining a room
    agora = Agora()

    token = agora.generate_token(data.id)

    call_user = User.query.get(data.id)

    return {"token": token, "username": call_user.username, "avatar": call_user.avatar}


