from sqlalchemy.orm import Session
#from db.models import Day
from fastapi import APIRouter, Depends
from . import schemas
from db.db import engine, SessionLocal
from sqlalchemy.orm import Session
from db.models import Day
from db import models


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
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/calender/days/")
async def how_many_bottles(request: schemas.Day, db: Session = Depends(get_db)):
    new_day = Day(date=request.date, bottles=request.bottles)
    payload = {}
    if new_day.bottles > 0:
        payload["marked"] = False
        new_day.marked = False

    else:
        payload["marked"] = True
        new_day.marked = True

    db.add(new_day)
    db.commit()
    db.refresh(new_day)
    return(payload)

@router.get("/calender/days/") #to get all the dates and their responses
def all(db:Session = Depends(get_db)):
	days = db.query(models.Day).all()
	return days
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
