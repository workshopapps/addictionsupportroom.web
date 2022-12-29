from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.models import User
from db.db import get_db
from fastapi.requests import Request
from .schema import EmergencyResponseModel
from typing import List
# from .. import deps
from db.models import Emergency


router = APIRouter()


class NewEmergency(BaseModel):
    username: str


@router.get("/emergencies")
def all_emergencies(db: Session = Depends(get_db)):
    #return a list of all existing emergencies
    emergencies = db.query(User).all()

    return emergencies


@router.get("/emergencies/{username}",
            status_code=status.HTTP_200_OK,
            responses={
                424: {
                    "description": "Error. Intention to relapse not recorded."
                },
                405: {
                    "description": "Method not allowed"
                },
                204: {
                    "description": "User not found"
                }
            })
def get_user_details(username: str,
                     request: Request,
                     db: Session = Depends(get_db)):
    """ Gets the details of a user facing a relapse emergency
        
        Args:
				username: A user's username (Path parameter)
				
		Returns:
				A JSON response containing the status code and message
                {
                    "status_code": 201,
                    "detail": " ",
                    "user": user_details
                    }   
	    Raises:
                HTTPException [405]: Method not allowed
                HTTPException [204]: User not found
                HTTPException [400]: Bad request
    """
    # to test. mock data.
    # user1 = User(username="lion", avatar="lion", hashed_password="lion")
    # db.add(user1)
    # db.commit()

    if request.method == "GET":

        if type(username) == str:

            user = db.query(User).filter(User.username == username).first()

            if not user:
                return {
                    "status_code": status.HTTP_204_NO_CONTENT,
                    "detail": "User " + username + " not found"
                }

            user_details = {
                "username": user.username,
                "avatar": user.avatar,
                "is_active": user.is_active,
                "date_added": user.date_added,
                "last_relapse_date": user.last_relapse_date
            }

            return {
                "status_code": status.HTTP_200_OK,
                "detail": "User " + username + " found",
                "user_details": user_details
            }

        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Bad request")

    else:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail="Method not allowed")



@router.get('/current-emergencies', name='All Current Emergencies', response_model=List[EmergencyResponseModel])
def get_current_emergencies(db: Session = Depends(get_db)):
    '''
        This endpoint retrieves all the users that are <strong>about-to-relapse</strong>
    '''

    emergencies = db.query(Emergency).all()
    return emergencies  