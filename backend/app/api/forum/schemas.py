from pydantic import BaseModel
from datetime import datetime
from typing import List


class Post(BaseModel):
    id: int
    title: str
    message: str
    date_posted: datetime

    class Config():
        orm_mode = True

class UserModel(BaseModel): #### NOTE change the name of the class
    id: int
    username: str

    class Config():
        orm_mode = True

class PostComment(BaseModel):
    owner_id: int
    origin_post_id: int
    message: str
    date_posted: datetime

    class Config():
        orm_mode = True


# BASE
class PostBase(BaseModel):
    title: str
    message: str
    owner_id: int

class PostCommentBase(BaseModel):
    owner_id: int
    origin_post_id: int
    message: str


# RESPONSE MODEL
class PostResponseModel(BaseModel):
    id: int
    title: str
    message: str
    user: UserModel
    post_comments: List[PostComment] = []
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
    message: str
    date_posted: datetime

    class Config():
        orm_mode = True