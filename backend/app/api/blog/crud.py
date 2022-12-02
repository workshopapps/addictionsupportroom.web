from sqlalchemy.orm import Session
import models


def get_all_blogs(db: Session):
    all_blogs = db.query(models.Blog).all()
    return all_blogs
