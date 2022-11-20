from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api import deps
from db.models import Messages

router = APIRouter()


class Contact(BaseModel):
    username: str
    message: str


@router.post("/", status_code=201)
def contact(
    data: Contact,
    db: Session = Depends(deps.get_db)
):
    try:
        message = Messages(username=data.username, message=data.message)
        db.add(message)
        db.commit()
    except Exception:
        raise 

    return {
        "msg": "Message received"
    }