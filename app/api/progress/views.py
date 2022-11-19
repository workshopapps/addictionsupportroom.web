from api.example.schemas import ExampleSchema
from api.progress.services import ProgressService
from api.progress import schemas
from db.db import db_session
from db.models.example import Example
from db.models.progress import Day

from fastapi import APIRouter, Body, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/calender/days", response_model=list[ExampleSchema])
async def get_days(
    session: AsyncSession = Depends(db_session),
) -> list[Example]:
    progress_service = ProgressService(session=session)
    return await progress_service.get_all_progresss()

'''
markedDates={{
       "2020-09-15": { bottle: true, marked: true},
       "2020-09-05": { selected: true, marked: true, selectedColor: "blue" },
       }}/>
'''


# Key: day's date
# bottle: 0
# marked: True


'''
IF bottles == 0:
Did not take bottle
If bootles >0:
Took bottle
'''


@router.get("/calender/days/{id}", response_model=list[schemas.Day])
async def get_days(
    id: str,
    session: AsyncSession = Depends(db_session),
) -> list[schemas.Day]:
    progress_service = ProgressService(session=session)
    return await progress_service.get_all_progresss()


@router.post("/calender/days/")  # , response_model=schemas.Day)
async def mark_a_day(
    day: schemas.Day,
    session: AsyncSession = Depends(db_session),
) -> ProgressService:
    progress_service = ProgressService(session=session)
    day = await progress_service.mark_a_day(day)
    return day
