from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import deps
from db.models import User
from .schema import ResponseModel
from fastapi.requests import Request

router = APIRouter()

class NewEmergency(BaseModel):
    username: str


@router.get(
    "/emergencies",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseModel,
    responses={
        204: {"description": "No emergencies at this time"},
        424: {"description": "Error querying database"},
        405: {"description": "Method not allowed"},
    }
    )
def all_emergencies(request: Request, db: Session = Depends(deps.get_db)):
    """ Returns a list of all existing emergencies
				
		Returns:
				A JSON response containing the status code, event, and success status.
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
				HTTPException [424]: Feedback not added
                HTTPException [405]: Method not allowed
                HTTPException [400]: Bad request
	"""
    if request.method == "GET":

        try:
            # # to test (add mock data)
            # user1 = User(username="lion", avatar="lion", hashed_password="lion")
            # user2 = User(username="lion2", avatar="lion", hashed_password="lion")
            # user3 = User(username="lion3", avatar="lion", hashed_password="lion")
            # db.add(user1)
            # db.add(user2)
            # db.add(user3)
            # db.commit()
    

            emergencies = db.query(User).all()

            # #to delete mock data
            # db.delete(user1)
            # db.delete(user2)
            # db.delete(user3)
            # db.commit()
            
            if emergencies == []:
                return ResponseModel(status=status.HTTP_204_NO_CONTENT, message="No emergencies at this time", data=emergencies)
        
        except:
            raise HTTPException(
                status_code=status.HTTP_424_FAILED_DEPENDENCY,
                detail="Error querying database"
            )

        return ResponseModel(status=status.HTTP_200_OK, message=(str(len(emergencies)) + " emergencies at this time"), data=emergencies)
    
    else:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Method not allowed."
        )