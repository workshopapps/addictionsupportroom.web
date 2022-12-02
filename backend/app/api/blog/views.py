from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from .crud import get_all_blogs, get_detail_blog

router = APIRouter()



@router.get('/')
def all_blogs(db: Session = Depends(get_db)):
    '''
    This endpoint is for getting all the blogs in the database
    '''
    blogs = get_all_blogs(db)
    return blogs



@router.get('/blogs/{id}')
def detail_blog(id: int, db: Session = Depends(get_db)):
    '''
    This endpoint is for getting a the blog in the database

    **id** - this field is required
    '''
    try: 
        blog = get_detail_blog(db=db, blog_id=id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"there is no blog with id: {id}")
    return blog