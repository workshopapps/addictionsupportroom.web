from typing import Any, List
import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, OAuth2AuthorizationCodeBearer
from sqlalchemy.orm import Session
from db.models import Relapse, Streak, Month
from api import deps
from .schemas import RelapseBase, RelapseCreate, RelapseInDB
from db.models import User

from .crud import relapse, create_relapse_with_user
from fastapi.encoders import jsonable_encoder

router = APIRouter()

auth_scheme = HTTPBearer()

months = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}


@router.post("/")
async def create_relapse(
    *,
    db: Session = Depends(deps.get_db),
    relapse_in: RelapseCreate,
    current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme)
) -> Any:
    """
    Create Relapse
    """

    # Create Month History, if it doesn't exist
    try:
        month_title = f'{months[str(relapse_in.month)]} {relapse_in.year}'
    except:
        return {
            "status_code": 400,
            "message": "Invalid month value",
        }
    month_history = db.query(Month).filter(
        Month.user == current_user.id,
        Month.title == month_title,
    ).first()

    if month_history is None:
        month_history = Month()
        month_history.user = current_user.id
        month_history.title = month_title
        db.add(month_history)
        db.commit()
        db.refresh(month_history)

    new_relapse = relapse.create_with_user(
        db=db,
        obj_in=relapse_in,
        user_id=current_user.id,
        month_id=month_history.id,
    )
    # new_relapse = create_relapse_with_user(db=db, user_id=current_user.id, relapse=relapse_in)
    user_streak = db.query(Streak).filter(
        Streak.user == current_user.id).first()
    if user_streak:
        user_streak.last_relapse = new_relapse
        db.commit()
        db.refresh(user_streak)
    else:
        user_streak = Streak(last_relapse=new_relapse.id, user=current_user.id)
        db.add(user_streak)
        db.commit()
        db.refresh(user_streak)
    return new_relapse


@router.get("/")
async def read_relapses(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme)
) -> Any:
    """
    Retrieve Relapse Days
    """
    # relapses = relapse.get_multi_by_user(db=db, user_id=current_user.id, skip=skip, limit=limit)
    relapses = db.query(Relapse).filter(Relapse.user == current_user.id).all()
    return relapses


@router.get("/milestone")
async def read_streaks(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme)
) -> Any:
    """
    Get a user milestone
    """
    user_streak = db.query(Streak).filter(
        Streak.user == current_user.id).first()
    user_streak.current_date = datetime.date.today()
    db.commit()
    db.refresh(user_streak)
    D = datetime.datetime.strptime(
        user_streak.current_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
    start_date = datetime.datetime.strptime(
        user_streak.start_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
    milestone_days = D - start_date
    user_streak.clean_days = milestone_days.days
    db.commit()
    db.refresh(user_streak)
    data = jsonable_encoder(user_streak)
    data["milestone_days"] = milestone_days.days
    return data
