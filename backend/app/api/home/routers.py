from random import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.home import schemas, crud
from db.db import get_db
from . import quotes



router = APIRouter()


@router.post("/emotions")
async def post_emotion(request):
    if request == "happy":
        return (quotes.happy[random.randint(0, 2)])
    elif request == "sober":
        return (quotes.sober[random.randint(0, 2)])
    elif request == "defeated":
        return (quotes.defeated[random.randint(0, 2)])
    elif request == "angry":
        return (quotes.angry[random.randint(0, 2)])
    else:
        return (quotes.confused[random.randint(0, 2)])

@router.get("/notes/", response_model=list[schemas.ShowNote])
def get_all_notes(db: Session=Depends(get_db)):
    notes = crud.get_all_notes(db=db)
    return notes



@router.post("/notes/create")
def create_note(note: schemas.Note, db: Session=Depends(get_db)):
    db_note = crud.create_note(db=db, note=note)
    return db_note



@router.get("/notes/today", response_model=list[schemas.ShowNote])
def get_all_notes_created_today(db: Session=Depends(get_db)):
    notes = crud.get_all_notes_created_today(db=db)
    return notes



@router.get("/notes/{note_id}", response_model=schemas.ShowNote)
def get_specific_note(note_id: int, db: Session=Depends(get_db)):
    note = crud.get_specific_note(db=db, note_id=note_id)
    return note



@router.delete("/notes/delete/{note_id}")
def delete_note(note_id: int, db: Session=Depends(get_db)):
    note = crud.delete_note(db=db, note_id=note_id)
    return note



@router.put("/notes/update/{note_id}")
def update_note(note_id: int, note: schemas.Note, db: Session=Depends(get_db)):
    note = crud.update_note(db=db, note_id=note_id, note=note)
    return note
