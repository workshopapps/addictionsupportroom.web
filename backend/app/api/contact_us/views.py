from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from api import deps
from db.models import ContactusMessages

from email.message import EmailMessage
import ssl
import smtplib

router = APIRouter()

APP_PASSWORD = "vwpoedpavesodepe"
TEAM_EMAIL = "crankshaft3182@gmail.com"


class Contact(BaseModel):
    name: str
    email: str | None = Field(
        default="contactUs@app.soberpal.com",
        example="This an optional email address used to identify the user from the web",
    )
    message: str
    user_id: str | None = Field(
        example="This an optional user_id used to identify the user from the mobile app"
    )


@router.post("/", status_code=201)
def contact(data: Contact, db: Session = Depends(deps.get_db)):
    if not data.user_id:
        data.user_id = data.email

    # Add contact message to database
    try:
        message = ContactusMessages(
            name=data.name, user_id=data.user_id, message=data.message
        )
        db.add(message)
        db.commit()
    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Couldn't add message",
        )

    # Send contact message to team email

    subject = f"Contact Message from {data.name}"
    body = f"""
    From: {data.user_id}
    
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

    return {"msg": "Message received"}
