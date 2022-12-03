from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from .crud import get_detail_blog, get_all_blogs

router = APIRouter()



@router.get('/')
def all_blogs():
    '''
    This endpoint is for getting all the blogs related to health froma blog site api 
    
    NOTE: this site is always updating their data that's why I'm not storing it in the database 
    '''
    result = get_all_blogs()
    return result



@router.get('/blogs/{id}')
def detail_blog(id: int):
    '''
    This endpoint is for getting a the blog in the database

    **id** - this field is required
    '''
    blog = get_detail_blog(id)
    if blog:
        return blog
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"there is no blog with id: {id}")