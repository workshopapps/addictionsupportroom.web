from fastapi import APIRouter, HTTPException, status, Depends
from api import deps
from db.models import User
from fastapi.requests import Request
from typing import Union
from sqlalchemy.orm import Session



router = APIRouter()

@router.put("/edit/{username}")
def edit_user_profile(username : str, db: Session = Depends(deps.get_db), user_name : str = None, avatar : str = None):

    user = db.query(User).filter(User.username==username).first()

    old_user_profile = {
        "username": user.username,
        "avatar": user.avatar
    }

    if user_name:
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

    return {
        "old_user_profile": old_user_profile,
        "new_user_profile": new_user_profile
    }