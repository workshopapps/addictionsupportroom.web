from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Post(BaseModel):
    id: int
    message: str
    date_posted: datetime

    class Config():
        orm_mode = True

class UserModel(BaseModel): #### NOTE change the name of the class
    id: int
    username: str
    avatar: str

    class Config():
        orm_mode = True

class PostComment(BaseModel):
    owner: UserModel
    origin_post: Post
    comment: str
    date_posted: datetime

    class Config():
        orm_mode = True


# BASE
class PostBase(BaseModel):
    message: str

class PostCommentBase(BaseModel):
    origin_post_id: int = 1
    comment: str


# RESPONSE MODEL
class PostResponseModel(BaseModel):
    '''
    A Pydantic class that defines the message response schema for fetching posts
    '''
    id: int
    message: str
    user: UserModel 
    post_comments: List[PostComment] = []
    num_of_comments: Optional[str] = '0 comments'
    date_posted: datetime

    class Config():
        orm_mode = True

class UserResponseModel(BaseModel):
    username: str
    posts: List[Post] = []
    post_comments: List[PostComment] = []

    class Config():
        orm_mode = True

class PostCommentResponseModel(BaseModel):
    owner: UserModel
    origin_post: Post
    comment: str
    date_posted: datetime

    class Config():
        orm_mode = True