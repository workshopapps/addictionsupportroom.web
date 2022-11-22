from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import deps
from db.models import Messages

router = APIRouter()


class Contact(BaseModel):
    name: str
    email: str
    message: str


@router.post("/", status_code=201)
def contact(
    data: Contact,
    db: Session = Depends(deps.get_db)
):

    # Add contact message to database
    try:
        message = Messages(name=data.name, email=data.email, message=data.message)
        db.add(message)
        db.commit()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Couldn't add message")

    return {
        "msg": "Message received"
    }
