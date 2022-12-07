from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.db import get_db
from .schemas import PostBase, PostResponseModel, PostCommentBase, PostCommentResponseModel
from .crud import (
    create_post, 
    create_post_comment, 
    get_all_post, 
    get_post
)
from typing import List


router = APIRouter()


## POST
@router.post('/', response_model=PostResponseModel)
def create_post_ED(request: PostBase, db: Session = Depends(get_db)):
    return create_post(db, request)

@router.get('/', response_model=List[PostResponseModel])
def get_all_post_ED(db: Session = Depends(get_db)):
    return get_all_post(db)

@router.get('/{id}', response_model=PostResponseModel)
def get_post_ED(id: int, db: Session = Depends(get_db)):
    return get_post(db, id)


## COMMENT
@router.post('/comment/', response_model=PostCommentResponseModel)
def create_post_comment_ED(request: PostCommentBase, db: Session = Depends(get_db)):
    return create_post_comment(db, request)