import datetime
import random
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.home import schemas, crud
from db.models import Emergency, User
from db.db import get_db
from . import quotes
from api import deps
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

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
def get_all_notes(db: Session = Depends(get_db),
                  current_user: User = Depends(deps.get_current_user)):
    """
    Gets all notes
    Returns:
        [
            {
                "created_at": "2022-12-07T07:57:30.651773",
                "id": 1,
                "updated_at": "2022-12-07T07:57:30.651773",
                "title": "Sample title.",
                "description": "This is an example."
            },
            {
                "created_at": "2022-12-07T07:59:32.271965",
                "id": 2,
                "updated_at": "2022-12-07T07:59:32.271965",
                "title": "Sample title.",
                "description": "This is an example."
            },
            {
                "created_at": "2022-12-07T08:01:40.388906",
                "id": 3,
                "updated_at": "2022-12-07T08:01:40.388906",
                "title": "Sample title.",
                "description": "This is an example."
            },
            {
                "created_at": "2022-12-07T08:05:20.022338",
                "id": 4,
                "updated_at": "2022-12-07T08:05:20.022338",
                "title": "Sample title.",
                "description": "This is an example."
            },
            {
                "created_at": "2022-12-07T08:06:17.262372",
                "id": 5,
                "updated_at": "2022-12-07T08:06:17.262372",
                "title": "Sample title.",
                "description": "This is an example."
            }
        ]
    Raises:
            HTTPException [401]: Unauthorised
    """
    notes = crud.get_all_notes(db=db)
    return notes


@router.post("/notes/create", response_model=schemas.Note, 
    status_code=status.HTTP_201_CREATED, 
    responses={
        404: {"description": "not authenticated"}
    })
def create_note(note: schemas.NoteCreate,
                db: Session = Depends(get_db),
                current_user: User = Depends(deps.get_current_user)):
    """
    Creates a Note by a user.
    
    Args: 
        note: Pydantic schema to define note parameters.

    Returns:
        {
            "created_at": "2022-12-07T08:06:17.262372",
            "id": 5,
            "updated_at": "2022-12-07T08:06:17.262372",
            "title": "Sample title.",
            "description": "This is an example."
        }
    Raises:
        HTTPException [401]: Unauthorised
        HTTPException [424]: message
    """

    db_note = crud.create_note(db=db, note=note)
    if not db_note:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": "Note not created"})

    response = JSONResponse(content=jsonable_encoder(db_note), status_code=status.HTTP_201_CREATED)
    return response


@router.get("/notes/today")  #  response_model=list[schemas.ShowNote]
def get_all_notes_created_today(db: Session = Depends(get_db),
                                current_user: User = Depends(
                                    deps.get_current_user)):
    notes = crud.get_all_notes_created_today(db=db)
    return notes


@router.get(
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Successful Response"},
        404: {"description": "Note Not Found"},
        422: {"description": "Validation Error"}
        })  #  response_model=schemas.ShowNote
def get_specific_note(note_id: int, db: Session = Depends(get_db)):
    """
    Fetches a specific note using the given note id.
    
    Args:
    
        note_id (int): note id
        
        db (Session, optional): Database. Defaults to Depends(get_db).
        
    Returns:
    
        {
            "id": note_id(int),
            "title": title of the note (str),
            "description": content of the note (str),
            "created_at": date the  note was created (datetime),
            "updated_at": date the note was updated (datetime)
        }
        
    Raises:
    
        HTTPException [404]: There's no note with id: {note_id}
    
        HTTPException [422]: Validation Error

    """
    note = crud.get_specific_note(db=db, note_id=note_id)
    return note


@router.delete("/notes/delete/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    """
    Deletes a specific note given the note id

    Args:
    
        note_id (int): note id
        
        db (Session, optional): Database. Defaults to Depends(get_db).

    Returns:

        {
            "id": note_id(int),
            "title": title of the note (str),
            "description": content of the note (str),
            "created_at": date the  note was created (datetime),
            "updated_at": date the note was updated (datetime)
        }
        
    Raises:
    
        HTTPException [404]: There's no note with id: {note_id}
        
    """
    note = crud.delete_note(db=db, note_id=note_id)
    return note


@router.put("/note/edit/{note_id}")
def update_note(note: schemas.Note,
                note_id: int,
                db: Session = Depends(get_db)):
    """
    Updates a note given the note's id. The note's description gets updated with the new note.

    Args:
    
        note (schemas.Note): New note.
        
        note_id (int): Note id.
        
        db (Session, optional): Database. Defaults to Depends(get_db).

    Returns:
    
        {
            "id": note_id(int),
            "title": title of the note (str),
            "description": content of the note (str),
            "created_at": date the  note was created (datetime),
            "updated_at": date the note was updated (datetime)
        }
        
    Raises:
    
        HTTPException [404]: There's no note with id: {note_id}
    """
    note = crud.update_note(db=db, note_id=note_id, note=note)
    return note


# TODO: fix this
# @router.put("/notes/update/{note_id}")
# def update_note(note_id: int,
#                 note: schemas.Note,
#                 db: Session = Depends(get_db)):
#     note = crud.update_note(db=db, note_id=note_id, note=note)
#     return 'note'
