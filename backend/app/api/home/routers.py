import datetime
import random
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.home import schemas, crud
from db.models import Emergency, User
from db.db import get_db
from . import quotes
from api import deps
from.schemas import Emotion, ResponseModel
from fastapi.requests import Request

router = APIRouter()


@router.post(
    "/emotions",
    status_code=status.HTTP_200_OK,
    responses={
        424: {"description": "Feedback not added"},
        405: {"description": "Method not allowed"},
        400: {"description": "Bad request"}
    }
    )
def post_emotion(emotion:Emotion, request:Request):
    """
    Post a variety of emotions, and get a Quote as a response
    Emotions can be either of these:
    [happy, sober, defeated, angry, confused]
    """
    """ Returns a quote to the user

		Collects the user's emotion from the request and returns a JSON response

		Args:
				emotion: A string about the user's mood
				
		Returns:
				A JSON response containing the status code, message, and data
                {
                    "status": 201,
                    "event": "add_new_feedback",
                    "success": true,
                    "data": {
                        "rating": Integer,
                        "description": Description,
                        "created_at": Datetime
                    }
                    }   
	    Raises:
				HTTPException [424]: Quote not found
                HTTPException [405]: Method not allowed
                HTTPException [400]: Bad request
	"""
    if request.method == "POST":

        try:
            if emotion.emotion == "happy":
                quote = quotes.happy[random.randint(0, 2)]

            elif emotion.emotion == "sober":
                quote = quotes.sober[random.randint(0, 2)]

            elif emotion.emotion == "defeated":
                quote = quotes.defeated[random.randint(0, 2)]

            elif emotion.emotion == "angry":
                quote = quotes.angry[random.randint(0, 2)]
    
            elif emotion.emotion == "confused":
                quote = quotes.confused[random.randint(0, 2)]
            else:
                quote = None
            
            if quote != None:
                return ResponseModel(status=status.HTTP_200_OK, message="Quote", data=quote)

            elif quote == None:
                print("here")
                return {
                    "status_code": status.HTTP_200_OK,
                    "message": "Emotion not registered"
                }
    
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Bad Request"
            )
    
    else:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Method not allowed"
        )


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
    notes = crud.get_all_notes(db=db)
    return notes


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
def delete_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(deps.get_current_user)):
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
