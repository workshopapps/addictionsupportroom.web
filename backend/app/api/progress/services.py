from api.example import schemas
from db.models import Example, Streak, User
from sqlalchemy import select
from sqlalchemy import desc
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import datetime



class ExampleService:
    # def __init__(self, session: AsyncSession = Depends(db_session)):
    #     self.session = session

    async def get_all_examples(self, db: Session) -> list[schemas.Examples]:
        examples = db.query(Example).all()

        return examples

    def create_example(self, db: Session, data) -> Example:
        example = Example(**data.dict())
        db.add(example)
        db.commit()
        db.refresh(example)

        return example


def get_all_users_streak(db: Session):
    """ 
    This function return all users with respect to the number of clean days if not return an empty list like this []
    """
    ranks = db.query(Streak).order_by(desc(Streak.clean_days)).all()
    
    return ranks


def get_top_20_users_with_high_streaks(db: Session):
    top_ranks = db.query(Streak).order_by(desc(Streak.clean_days)).limit(20).all()
    return top_ranks
    
    

def get_auser_total_clean_days(streak_id: int, db: Session):
    streak = db.query(Streak).filter(Streak.id == streak_id).first()
    
    if not streak:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There's no streak with id: {streak_id}")
    return streak

    