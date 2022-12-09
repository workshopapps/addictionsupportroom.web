from fastapi import APIRouter, HTTPException, status, Depends
from api import deps
from db.models import User
from fastapi.requests import Request
from typing import Union
from sqlalchemy.orm import Session



router = APIRouter()



@router.put("/edit/{username}")
def edit_user_profile(request: Request, username : str, db: Session = Depends(deps.get_db), user_name : str = None, avatar : str = None):
    if request.method == "PUT":

        user = db.query(User).filter(User.username==username).first()

        if not user:
            return HTTPException(
                status_code=status.HTTP_204_NO_CONTENT,
                detail="User not found"
            )

        old_user_profile = {
            "username": user.username,
            "avatar": user.avatar
        }


        if user_name:
            username_exists = db.query(User).filter(User.username==user_name).first()

            if username_exists:
                # to check if the USER selects their current username
                if username_exists.username == user.username:
                    pass
                
                # what to do if USER selects a new username that is already existing on the database
                else:
                    return HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="Username already exists. Please choose another one"
                    )
            

            user.username = user_name
            db.commit()


        if avatar:
            user.avatar = avatar
            db.commit()


        db.refresh(user)


        new_user_profile = {
            "username": user.username,
            "avatar": user.avatar
        }

        user_profile = {
            "old_user_profile": old_user_profile,
            "new_user_profile": new_user_profile
        }


        return {
            "status_code": status.HTTP_201_CREATED,
            "detail": "Changes made",
            "user_profile": user_profile
        }
    
    else:
        return HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Method not allowed"
        )