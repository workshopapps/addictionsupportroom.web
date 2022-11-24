from services import ExampleService
from sqlalchemy.orm import Session
from db.models import Rank
from fastapi import APIRouter, Depends
from . import schemas
from sqlalchemy.orm import Session

from api import deps


router = APIRouter()

@router.get("/leaderboard/", response_model=list[schemas.Ranking])
async def create_example(
    data: schemas.Ranking,
    db: Session = Depends(deps.get_db),
):
    example = Rank()
    example.id = data.id
    example.username = data.username
    example.avatar = data.avatar
    example.start_date = data.start_date
    example.current_date = data.current_date
    example.clean_days = data.start_date - data.current_date
    
    db.add(example)
    db.commit()
    db.refresh(example)

    return example

