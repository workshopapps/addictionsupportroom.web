from fastapi import APIRouter, Depends
from . import crud
from sqlalchemy.orm import Session
from . import schemas
from db.db import get_db



router = APIRouter()



@router.get("/api/notes/")
def get_all_notes(db: Session=Depends(get_db)):
    notes = crud.get_all_notes(db=db)
    return notes



@router.post("/api/notes/create")
def create_note(note: schemas.Note, db: Session=Depends(get_db)):
    db_note = crud.create_note(db=db, note=note)
    return db_note



@router.get("/api/notes/today")
def get_all_notes_created_today(db: Session=Depends(get_db)):
    notes = crud.get_all_notes_created_today(db=db)
    return notes



@router.get("/api/notes/{note_id}")
def get_specific_note(note_id: int, db: Session=Depends(get_db)):
    note = crud.get_specific_note(db=db, note_id=note_id)
    return note



@router.delete("/api/notes/delete/{note_id}")
def delete_note(note_id: int, db: Session=Depends(get_db)):
    note = crud.delete_note(db=db, note_id=note_id)
    return note



@router.put("/api/notes/update/{note_id}")
def update_note(note_id: int, note: schemas.Note, db: Session=Depends(get_db)):
    note = crud.update_note(db=db, note_id=note_id, note=note)
    return note


