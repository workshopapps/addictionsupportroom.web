from sqlalchemy.orm import Session
from db.models import Blog


def get_all_blogs(db: Session):
    all_blogs = db.query(Blog).all()
    return all_blogs
