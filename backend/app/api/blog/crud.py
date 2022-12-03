from sqlalchemy.orm import Session
from db.models import Blog


def get_all_blogs(db: Session):
    all_blogs = db.query(Blog).all()
    return all_blogs

def get_detail_blog(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    return blog