from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from api.common.schemas import ResponseSchema
from api.auth.schemas import UserBase
from . import services
from fastapi import APIRouter, Depends
from . import schemas
from sqlalchemy.orm import Session
import datetime
from .schemas import GetAllHistoryResult, GetAllRanking, Ranking, SummarySchema, TotalCleanDays
from typing import Any

from .schemas import RelapseBase, RelapseCreate, RelapseInDB
from fastapi.security import HTTPBearer
from db.models import User, Streak, Relapse, Month
from fastapi.encoders import jsonable_encoder
from .crud import relapse, create_relapse_with_user

auth_scheme = HTTPBearer()

from api import deps

router = APIRouter()

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

milestones = [1, 7, 30, 90]


@router.post("/")
async def mark_a_day(
        *,
        db: Session = Depends(deps.get_db),
        relapse_in: RelapseCreate,
        current_user: User = Depends(deps.get_current_user),
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
    # Save the new relapse
    db.add(new_relapse)
    db.commit()
    db.refresh(new_relapse)

    user_streak = db.query(Streak).filter(
        Streak.user == current_user.id).first()
    if user_streak:
        user_streak.last_relapse_date = datetime.date.today
        db.commit()
    else:
        user_streak = Streak(
            last_relapse_date=datetime.date.today,
            user=current_user.id,
        )
        db.add(user_streak)
        db.commit()
    return new_relapse


@router.get("/", name='Get Relapses in a Month')
async def read_relapses(
        *,
        db: Session = Depends(deps.get_db),
        month: int = 1,
        year: int = 2022,
        current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve Relapse Days in a given month
    """
    # relapses = relapse.get_multi_by_user(db=db, user_id=current_user.id, skip=skip, limit=limit)
    relapses = db.query(Relapse).filter(
        Relapse.user == current_user.id,
        Relapse.month == month,
        Relapse.year == year,
    ).all()

    return relapses


@router.get(
    "/milestone",
    response_model=SummarySchema | ResponseSchema,
    responses={
        200: {
            "model": SummarySchema,
            "description": "A summary for user progress",
        },
        400: {
            "model": ResponseSchema,
            "description": "User not found.",
        },
    },
)
async def get_milestone(
        *,
        current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Get a user milestone
    Returns {clean_days: 1, milestone: 3}
    """

    # Get current user streak
    # Check for when the last relapse occured
    # Subtract today's date from last relapse
    # Check where the milestone for the date lie
    # Returns {clean_days: 1, milestone: 3}

    today = datetime.date.today()
    last_relapse_date = current_user.last_relapse_date

    difference = today - last_relapse_date

    clean_days = difference.days

    result = {
        "clean_days": clean_days,
        "milestone": 0,
    }

    for milestone in milestones:
        if clean_days <= milestone:
            result = {
                "clean_days": clean_days,
                "milestone": milestone,
            }
        break

    return result


@router.get(
    "/leaderboard/top",
    response_model=GetAllRanking | ResponseSchema,
    responses={
        200: {
            "model": GetAllRanking,
            "description": "A list of leaderboard for all user.",
        },
        400: {
            "model": ResponseSchema,
            "description": "User not found.",
        },
    },
)
async def get_leaderboard_top_rankings(
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Get a list of users toping the board
    
    """

    # Check user db & order by last relapse date

    users = db.query(User).order_by(User.last_relapse_date).limit(20).all()

    today = datetime.date.today()
    result = []

    for user in users:
        difference = today - user.last_relapse_date
        clean_days = difference.days
        result.append(
            Ranking(
                id=user.id,
                username=user.username,
                avatar=user.avatar,
                clean_days=clean_days,
            ))

    return {"status_code": 200, "result": result}


@router.get(
    "/leaderboard/all",
    response_model=GetAllRanking | ResponseSchema,
    responses={
        200: {
            "model": GetAllRanking,
            "description": "A list of leaderboard for all user.",
        },
        400: {
            "model": ResponseSchema,
            "description": "User not found.",
        },
    },
)
async def get_leaderboard_all_rankings(
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Get a list of all users and their rankings on the board.
    
    """

    # Check user db & order by last relapse date

    users = db.query(User).order_by(User.last_relapse_date).all()
    today = datetime.date.today()
    result = []

    for user in users:
        difference = today - user.last_relapse_date
        clean_days = difference.days
        result.append(
            Ranking(
                id=user.id,
                username=user.username,
                avatar=user.avatar,
                clean_days=clean_days,
            ))

    return {"status_code": 200, "result": result}


@router.get(
    "/leaderboard/user/total",
    response_model=TotalCleanDays | ResponseSchema,
    responses={
        200: {
            "model": TotalCleanDays,
            "description": "current user's total number of clean days.",
        },
        400: {
            "model": ResponseSchema,
            "description": "User not found.",
        },
    },
)
async def get_current_user_total_clean_days(
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Get the current user's total number of clean days.
    
    """

    # Check user db & order by last relapse date
    id = current_user.id

    users = db.query(User).get(id) 

    today = datetime.date.today()
    difference = today - users.last_relapse_date
    clean_days = difference.days
    result = []
    return {"status_code": 200, "clean_days": clean_days}


@router.get(
    "/summary",
    response_model=SummarySchema | ResponseSchema,
    responses={
        200: {
            "model": SummarySchema,
            "description": "A summary for user progress",
        },
        400: {
            "model": ResponseSchema,
            "description": "User not found.",
        },
    },
)
async def get_summary(
        current_user: User = Depends(deps.get_current_user), ) -> Any:
    """
    Get a user milestone
    Returns {clean_days: 1, milestone: 3}
    """

    # Get current user streak
    # Check for when the last relapse occured
    # Subtract today's date from last relapse
    # Check where the milestone for the date lie
    # Returns {clean_days: 1, milestone: 3}

    today = datetime.date.today()
    last_relapse_date = current_user.last_relapse_date

    difference = today - last_relapse_date

    clean_days = difference.days

    result = {
        "clean_days": clean_days,
        "milestone": 0,
    }

    for milestone in milestones:
        if clean_days <= milestone:
            result = {
                "clean_days": clean_days,
                "milestone": milestone,
            }
        break

    return result


@router.get(
    "/history/list",
    response_model=GetAllHistoryResult | ResponseSchema,
    status_code=201,
    name="list of history",
    responses={
        200: {
            "model": GetAllHistoryResult,
            "description": "A list of history for each user.",
        },
        400: {
            "model": ResponseSchema,
            "description": "User not found.",
        },
    },
)
async def history_list(
        currentUser: UserBase = Depends(deps.get_current_user),
        session: Session = Depends(deps.get_db),
):
    """
    The fetch history endpoint.

    Returns:
        GetAllHistoryResult: return a list of montths 
    """

    # Get all Months
    results = session.query(Month).all()
    # Sum up number of bottles taken
    result = []
    for month in results:
        # Number of bottles taken in a month
        bottle_count = 0
        for relapses in month.relapses:
            bottle_count += relapses.bottles_drank

        result.append(
            schemas.Months(
                title=month.title,
                bottle_count=bottle_count,
            ))

    return {"status_code": 200, "result": result}
