from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm.session import Session
from db.db import get_db
from .schemas import PostBase, PostResponseModel, PostCommentBase, PostCommentResponseModel, UserResponseModel
from .crud import PostClass
from typing import List
from db.models import User
from api.deps import get_current_user
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()


@router.post(
    '/', 
    status_code=201,
    name="Create a post",
    response_model=PostResponseModel
)
def create_post_EP(request: PostBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    '''
        This endpoint is for creating a post in the web community\n
        **message**  :  Required\n
    '''
    new_post = PostClass(current_user)
    return  new_post.create_post(db, request)


@router.get(
    '/', 
    status_code=200,
    name="Get All Post", 
    response_model=List[PostResponseModel]
)
def get_all_post_EP(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    '''
        This endpoint is for retrieving all posts in the web community
    '''
    all_posts = PostClass(current_user)
    return all_posts.get_all_post(db)


@router.get(
    '/{id}',
    status_code=200,
    name='Get A Post',
    response_model=PostResponseModel)
def get_post_EP(
    id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    '''
        This endpoint is for retrieving a post\n

        **id**  :  Required
    '''
    post_intance = PostClass(current_user)
    post = post_intance.get_post(db, id)
    if post:
        return post
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post of ID {id} does not exist')


@router.post(
    '/comment/',
    status_code=201,
    name='Create a comment in a post',
    response_model=PostCommentResponseModel)
def create_post_comment_EP(request: PostCommentBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    '''
        This endpoint is for creating a comment in a post in the web community\n
        **origin_post_id**  :  Required\n
        **message**  :  Required\n
    '''
    post_instance = PostClass(current_user)
    post = post_instance.create_post_comment(db, request)
    if post:
        return post
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post of ID {request.origin_post_id} does not exist and can not have comment')