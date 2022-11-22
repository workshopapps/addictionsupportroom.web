from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from sqlalchemy.orm import Session
from db.models import Day
from fastapi import APIRouter, Depends
from . import schemas

from sqlalchemy.orm import Session

from api import deps

router = APIRouter()


# @router.get("/", response_model=list[ExampleSchema])
# async def get_examples(
#     db: Session = Depends(deps.get_db),
# ) -> list[Example]:
#     example_service = ExampleService()
#     return await example_service.get_all_examples(db=db)


# @router.post("/", response_model=ExampleSchema)
# async def create_example(
#     data: Examples,
#     db: Session = Depends(deps.get_db),
# ) -> Example:
#     example_service = ExampleService()
#     example = example_service.create_example(db=db, data=data)
#     return example

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
