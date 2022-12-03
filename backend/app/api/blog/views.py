from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .crud import get_all_blogs
from api import deps

router = APIRouter()



@router.get('/')
def all_blogs(db: Session = Depends(deps.get_db)):
    '''
    This endpoint is for getting all the blogs in the database
    '''
    blogs = get_all_blogs(db)
    return blogs