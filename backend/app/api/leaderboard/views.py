from sqlalchemy.orm import Session
from db.models import Rank
from fastapi import APIRouter, Depends
from . import schemas, crud
from sqlalchemy.orm import Session
from db.db import get_db
from api import deps
# from typing import List


router = APIRouter()


@router.get("/api/leaderboard/", response_model=list[schemas.Ranking])
def get_all_streak(db: Session=Depends(deps.get_db)):
    ranks = crud.get_all_users_streak(db=db)
    return ranks



@router.get("/api/leaderboard/{streak_id}", response_model=schemas.Ranking)
def get_specific_streak(streak_id: int, db: Session=Depends(get_db)):
    streak = crud.get_specific_users_streak(db=db, streak_is=streak_id)
    return streak


