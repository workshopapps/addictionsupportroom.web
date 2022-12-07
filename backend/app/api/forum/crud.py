from db.db import get_db
from sqlalchemy.orm.session import Session
from .schemas import PostBase, PostCommentBase
from db.models import ForumPost, ForumPostComment


## POST
def create_post(db: Session, request: PostBase):
    new_post = ForumPost(
        title=request.title,
        message=request.message,
        user_id=request.owner_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_post(db: Session):
    posts = db.query(ForumPost).all()
    return posts

def get_post(db: Session, id: int):
    post = db.query(ForumPost).filter(ForumPost.id == id).first()
    return post


## COMMENT
def create_post_comment(db: Session, request: PostCommentBase):
    new_comment = ForumPostComment(
        owner_id=request.owner_id,
        origin_post_id=request.origin_post_id,
        message=request.message
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment