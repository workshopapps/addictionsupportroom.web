from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from sqlalchemy.orm import Session
from db.models import Day
from fastapi import APIRouter, Depends
from . import schemas

from sqlalchemy.orm import Session

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
