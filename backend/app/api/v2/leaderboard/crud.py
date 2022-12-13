from datetime import datetime
from sqlalchemy.orm import Session
from .leaderboard import schemas
from db.models import Rank
# from models import Rank
from fastapi import HTTPException, status


def get_all_users_streak(db: Session):
    """ 
    This function return all users with respect to the number of clean days if not return an empty list like this []
    """
    ranks = db.query(Rank).all()
    print(ranks)
    return ranks


def get_specific_users_streak(streak_id: int, db: Session):
    streak = db.query(Rank).filter(Rank.id == streak_id).first()

    if not status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There's no streak with id: {streak_id}")
    return streak