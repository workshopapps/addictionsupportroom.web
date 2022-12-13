from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from .. import deps
from sqlalchemy.orm import Session
from .schema import Feedback, ResponseModel
from db.models import Feedbacks

router = APIRouter()


@router.post("/add",
             status_code=status.HTTP_201_CREATED,
             response_model=ResponseModel,
             responses={
                 424: {
                     "description": "Feedback not added"
                 },
                 405: {
                     "description": "Method not allowed"
                 },
                 400: {
                     "description": "Bad request"
                 }
             })
def add_feedback(data: Feedback,
                 request: Request,
                 db: Session = Depends(deps.get_db)):
    """Adds a new feedback to the Feedback table.

		Collects a JSON request from the mobile frontend. Adds a rating and description with a unique ID to the database.

		Args:
				rating: An integer from 1 to 5 representing a rating of the app
				description: A string description about user's experience in detail.
				
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

    if request.method == "POST":

        try:
            rating = data.rating
            description = data.description

        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Bad request")

        try:
            new_feedback = Feedbacks(rating=rating, description=description)
            db.add(new_feedback)
            db.commit()

        except:
            raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,
                                detail="Feedback not added")

        # #to delete, since we are still testing
        # db.delete(new_feedback)
        # db.commit()

        return ResponseModel(status=status.HTTP_201_CREATED,
                             message="New Feedback added",
                             data=new_feedback.__dict__)

    else:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail="Method not allowed")
