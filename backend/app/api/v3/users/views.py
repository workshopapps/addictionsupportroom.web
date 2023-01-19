from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..deps import get_current_user, get_db
from db.models import User
from .schemas import ProfileResponseModel

router = APIRouter()


@router.get('/', name='User Profile', status_code=200, response_model=ProfileResponseModel)
async def profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    '''
        This enpoint is used to get the profile of a user.
    '''
    # print(await current_user)
    # user = current_user
    user = db.query(User).filter(User.id == current_user.id).first()
    return user
