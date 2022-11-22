from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import deps
from db.models import Messages

from email.message import EmailMessage
import ssl
import smtplib

router = APIRouter()

APP_PASSWORD = "vwpoedpavesodepe"
TEAM_EMAIL = "crankshaft3182@gmail.com"

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

    # Send contact message to team email

    subject = f"Contact Message from {data.name}"
    body = f"""
    From: {data.email}
    
    {data.message}
    """

    em = EmailMessage()
    em["From"] = data.email
    em["To"] = TEAM_EMAIL
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(TEAM_EMAIL, APP_PASSWORD)
        smtp.sendmail(TEAM_EMAIL, TEAM_EMAIL, em.as_string())

    return {
        "msg": "Message received"
    }
