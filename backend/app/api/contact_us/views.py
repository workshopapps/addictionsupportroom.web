from fastapi import APIRouter, Body, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from api import deps
from api.contact_us.schemas import NewsLetterEmail
from api.common.schemas import ResponseModel
from db.models import ContactusMessages
from db import models

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
        example=
        "This an optional email address used to identify the user from the web",
    )
    message: str
    user_id: str | None = Field(
        example=
        "This an optional user_id used to identify the user from the mobile app"
    )


examples = {
    "Web Site": {
        "summary": "Web Site",
        "description": "Example Request from Web Site.",
        "value": {
            'name': 'Ipaye Seyi',
            'email': 'seyi@app.com',
            'message': 'I am about to relapse'
        },
    },
    "Mobile App": {
        "summary": "Mobile App",
        "description": "Example Request from Mobile App",
        "value": {
            'name': 'Ipaye Seyi',
            'user_id': 30,
            'message': 'I am about to relapse'
        },
    },
}


@router.post("/", status_code=200, description='Send a message to the admin.')
def contact_us(
        data: Contact = Body(default=None, examples=examples),
        db: Session = Depends(deps.get_db),
):
    if not data.user_id:
        data.user_id = data.email

    # Add contact message to database
    try:
        message = ContactusMessages(name=data.name,
                                    user_id=data.user_id,
                                    message=data.message)
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


@router.post("/newsletter",
             status_code=200,
             description='Join the news letter')
def newsletter(
        data: NewsLetterEmail,
        db: Session = Depends(deps.get_db),
):

    email = models.NewsLetterEmail(email=data.email)
    db.add(email)
    db.commit()

    return ResponseModel.success(
        email,
        message='Successfully joined the newsletter',
    )
