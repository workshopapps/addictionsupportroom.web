from sqlalchemy.orm import Session
from . import models


def get_all_blogs(db: Session):
    all_blogs = db.query(models.Blog).all()
    return all_blogs


def get_detail_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    return blog