import datetime
import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..home import schemas, crud
from db.models import Emergency, User
from db.db import get_db
from . import quotes
from .. import deps
from ..common.schemas import ResponseModel

router = APIRouter()

@router.post("/emotions")
async def post_emotion(emotion: str):
    """
    Post a variety of emotions, and get a Quote as a response
    Emotions can be either of these:
    [happy, sober, defeated, angry, confused]
    """
    if emotion == "happy":
        return (quotes.happy[random.randint(0, 2)])
    elif emotion == "sober":
        return (quotes.sober[random.randint(0, 2)])
    elif emotion == "defeated":
        return (quotes.defeated[random.randint(0, 2)])
    elif emotion == "angry":
        return (quotes.angry[random.randint(0, 2)])
    elif emotion == "confused":
        return (quotes.confused[random.randint(0, 2)])
    else:
        return {"message": "Invalid emotion"}


@router.post("/relapse")
def about_to_relapse(currentUser: User = Depends(deps.get_current_user),
                     db: Session = Depends(deps.get_db)):

    #Add the user to the emergency database
    try:
        add_emergency = Emergency(name=currentUser.username,
                                  avatar=currentUser.avatar,
                                  created_at=datetime.datetime.utcnow())
        db.add(add_emergency)
        db.commit()
    except Exception as e:
        print(e.args)
        return {"error": "internal server error. try again later."}

    return {"success": "keep calm. someone will reach out soon."}


@router.get("/notes/")
def get_all_notes(token: str, db: Session = Depends(get_db)):

    current_user_id =(Depends(deps.get_current_user(token=token))).dependency

    current_user_notes = db.query(User).filter(User.id==current_user_id).first()

    return current_user_notes


@router.post("/notes/create")
def create_note(note: schemas.Note,
                db: Session = Depends(get_db),
                current_user: User = Depends(deps.get_current_user)):
    db_note = crud.create_note(db=db, note=note)
    return db_note


@router.get("/notes/today")  #  response_model=list[schemas.ShowNote]
def get_all_notes_created_today(db: Session = Depends(get_db),
                                current_user: User = Depends(
                                    deps.get_current_user)):
    notes = crud.get_all_notes_created_today(db=db)
    return notes


@router.get(
    "/notes/{note_id}", )  #  response_model=schemas.ShowNote
def get_specific_note(note_id: int,
                      db: Session = Depends(get_db),
                      current_user: User = Depends(deps.get_current_user)):
    note = crud.get_specific_note(db=db, note_id=note_id)
    return note


@router.delete("/notes/delete/{note_id}")
def delete_note(note_id: int,
                db: Session = Depends(get_db),
                current_user: User = Depends(deps.get_current_user)):
    note = crud.delete_note(db=db, note_id=note_id)
    return note


@router.put("/note/edit/{note_id}")
def update_note(note: schemas.Note,
                note_id: int,
                db: Session = Depends(get_db)):
    note = crud.update_note(db=db, note_id=note_id, note=note)
    return note


# TODO: fix this
# @router.put("/notes/update/{note_id}")
# def update_note(note_id: int,
#                 note: schemas.Note,
#                 db: Session = Depends(get_db)):
#     note = crud.update_note(db=db, note_id=note_id, note=note)
#     return 'note'


@router.post('/faq', name='Have a question?')
def ask_question(request: schemas.LeadCollectedModel,
                 db: Session = Depends(get_db)):
    '''
    This endpoint is for collecting email from the user.\n

    Args:\n
    \temail  :   Required

    Response:\n
    \t{
        \t"status": "success",
        \t"message": "Successfully joined the newsletter",
        \t"data": {
        \t    "id": 1,
        \t    "email": "askquestion@app.soberpal.com"
        \t}
    \t}
    '''
    email = crud.create_lead_email(db, request)

    return ResponseModel.success(
        email,
        message='Successfully joined the newsletter',
    )


@router.get('/faq', name='get all email')
def get_all_email(db: Session = Depends(get_db)):
    emails = crud.get_all_email(db)

    return ResponseModel.success(
        emails,
        message='ok',
    )