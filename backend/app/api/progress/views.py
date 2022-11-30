from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from . import services
from sqlalchemy.orm import Session
from db.models import Day
from fastapi import APIRouter, Depends
from . import schemas
from sqlalchemy.orm import Session
import datetime


from typing import Any
from .schemas import RelapseBase, RelapseCreate, RelapseInDB
from fastapi.security import HTTPBearer, OAuth2AuthorizationCodeBearer
from fastapi.encoders import jsonable_encoder
from db.models import User, Streak, Relapse
from fastapi.encoders import jsonable_encoder
from .crud import relapse, create_relapse_with_user
auth_scheme = HTTPBearer()

from api import deps
router = APIRouter()

@router.post("/calender/days/", response_model=schemas.Day)
async def create_example(
    data: schemas.Day,
    db: Session = Depends(deps.get_db),
):
    example = Day()
    example.day_id = data.day_id
    example.bottles = data.bottles
    example.marked = data.marked
    db.add(example)
    db.commit()
    db.refresh(example)

    return example



# @router.post("/calender/days/")  # , response_model=schemas.Day)
# async def mark_a_day(
#     day: schemas.Day,
#     session: AsyncSession = Depends(db_session),
# ) -> ProgressService:
#     progress_service = ProgressService(session=session)
#     day = await progress_service.mark_a_day(day)
#     return day

# @router.get("/calender/days/{id}", response_model=list[schemas.Day])
# async def get_days(
#     id: str,
#     session: AsyncSession = Depends(db_session),
# ) -> list[schemas.Day]:
#     progress_service = ProgressService(session=session)
#     return await progress_service.get_all_progresss()



@router.get("/leaderboard", response_model=list[schemas.Ranking])
def get_all_streaks(db: Session=Depends(deps.get_db)):
    ranks = services.get_all_users_streak(db=db)
    return ranks


@router.get("/leaderboard/top", response_model=list[schemas.Ranking])
def get_top_ranking(db: Session=Depends(deps.get_db)):
    top_ranks = services.get_top_20_users_with_high_streaks(db=db)
    return top_ranks


@router.get("/leaderboard/total_clean_days/{streak_id}", response_model=schemas.Ranking)
def get_specific_streak(streak_id: int, db: Session=Depends(deps.get_db)):
    streak = services.get_auser_total_clean_days(db=db, streak_id=streak_id)
    return streak


@router.post("/")
async def create_relapse(
    *, db: Session = Depends(deps.get_db), relapse_in: RelapseCreate,
    current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme)
    ) -> Any:
    """
    Create Relapse
    """
    new_relapse = relapse.create_with_user(db=db, obj_in=relapse_in, user_id=current_user.id)
    # new_relapse = create_relapse_with_user(db=db, user_id=current_user.id, relapse=relapse_in)
    user_streak = db.query(Streak).filter(Streak.user==current_user.id).first()
    if user_streak:
        user_streak.last_relapse = new_relapse.id
        db.commit()
        db.refresh(user_streak)
    else:
        user_streak = Streak(last_relapse=new_relapse.id, user=current_user.id)
        db.add(user_streak)
        db.commit()
        db.refresh(user_streak)
    data = jsonable_encoder(new_relapse)
    return data

@router.get("/")
async def read_relapses(*,
    db: Session = Depends(deps.get_db),  skip: int = 0,
    limit: int = 100, current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme))-> Any:
    """
    Retrieve Relapse Days
    """
    # relapses = relapse.get_multi_by_user(db=db, user_id=current_user.id, skip=skip, limit=limit)
    relapses = db.query(Relapse).filter(Relapse.user==current_user.id).all()
    return relapses 


@router.get("/milestone")
async def read_streaks(*,
    db: Session = Depends(deps.get_db),  skip: int = 0,
    limit: int = 100, current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme)) -> Any:
    """
    Get a user milestone
    """
    user_streak = db.query(Streak).filter(Streak.user==current_user.id).first()
    user_streak.current_date = datetime.date.today()
    db.commit()
    db.refresh(user_streak)
    D = datetime.datetime.strptime(user_streak.current_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
    start_date = datetime.datetime.strptime(user_streak.start_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
    milestone_days = D-start_date
    data = jsonable_encoder(user_streak)
    data["milestone_days"] = milestone_days.days
    return data