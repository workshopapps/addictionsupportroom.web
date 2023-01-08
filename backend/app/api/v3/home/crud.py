from datetime import datetime
from sqlalchemy.orm import Session
from . import schemas
from . import models
from datetime import datetime
from fastapi import HTTPException, status, Depends
from .. import deps
from db.models import Note


def create_note(token: str, db: Session, note: schemas.Note):
    """ 
    This function is used to create new note
    """

    current_user_id = (Depends(deps.get_current_user(token=token))).dependency

    db_note = Note(user_id=current_user_id,
                          title=note.title,
                          description=note.description,
                          created_at=datetime.utcnow(),
                          updated_at=datetime.utcnow())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note


def get_all_notes_created_today(db: Session):
    """
    This function return the all the notes created  daily
    if not Note then it will return empty list like this []
    
    """
    notes = db.query(models.Note).all()
    return notes


def get_specific_note(note_id: int, db: Session):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"there is no note with id: {note_id}")
    return note


def delete_note(note_id: int, db: Session):
    """ 
     This function delete the not based on id if there is no Note with that id.
     Then it will raise Exception HTTP_404_NOT_FOUND with a message
     there is no note with id: number
    """
    note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"there is no note with id: {note_id}")
    db.delete(note)
    db.commit()
    return note


def update_note(note_id: int, note: schemas.Note, db: Session):
    """ 
     This function update the not based on id if there is no Note with that id.
     Then it will raise Exception HTTP_404_NOT_FOUND with a message
     there is no note with id: number
    """
    note_in = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"there is no note with id: {note_id}")
    note_in.title = note.title
    note_in.description = note.description
    db.commit()
    db.refresh(note_in)
    return note


def get_all_notes(db: Session):
    """ 
    This function return all Note if not return an empty list like this []
    """
    notes = db.query(models.Note).all()
    return notes


def create_lead_email(db: Session, request: schemas.LeadCollectedModel):
    email_inst = models.LeadCollected(email=request.email)
    db.add(email_inst)
    db.commit()
    db.refresh(email_inst)
    return email_inst


def get_all_email(db: Session):
    emails = db.query(models.LeadCollected).all()
    return emails