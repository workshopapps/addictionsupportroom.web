from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from . import services
from sqlalchemy.orm import Session
#from db.models import Day
from fastapi import APIRouter, Depends
from . import schemas
from sqlalchemy.orm import Session
import datetime


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
    db.refresh(new_day)
    return(payload)

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