from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from api.common.schemas import ResponseSchema
from api.auth.schemas import UserBase
from . import services
from sqlalchemy.orm import Session
from db.models import Month

from fastapi import APIRouter, Depends, HTTPException, status
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
from db.schemas import ResponseModel
from starlette.responses import JSONResponse

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


@router.post("/", response_model=RelapseCreate)
async def mark_a_day(
        *,
        db: Session = Depends(deps.get_db),
        relapse_in: RelapseCreate,
        current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Create Relapse

    Returns:
        {
            "status": "success",
            "message": "relapse date updated",
            "data": {
                "new_relapse_date": "2022-12-08"
            }
        }

        or 

        {
            "status": "success",
            "message": "num of bottles updated",
            "data": {
                "month": 12,
                "day": 1,
                "bottles_drank": 1,
                "month_id": 1,
                "id": 1,
                "year": 2022,
                "user": 1
            }
        }

        {
            "status_code": 400,
            "message": "Invalid month value",
        }

    """
    if relapse_in.day > 31 or relapse_in.month > 12 or len(str(relapse_in.year)) > 4:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={
                "message": "out of bounds"
                }
            )
    relapse_in_db = db.query(Relapse).filter(Relapse.user==current_user.id, 
        Relapse.day==relapse_in.day, Relapse.month==relapse_in.month, Relapse.year==relapse_in.year).first()
    if relapse_in_db:
        relapse_in_db.bottles_drank = relapse_in.bottles_drank
        db.commit()
        db.refresh(relapse_in_db)
        data = jsonable_encoder(relapse_in_db)
        # data["message"] = "num of bottles updated"
        return JSONResponse(
            content=ResponseModel.success(data=data, message="num of bottles updated"),
            status_code=status.HTTP_200_OK
        )
    # Create Month History, if it doesn't exist
    try:
        month_title = f'{months[str(relapse_in.month)]} {relapse_in.year}'
    except:
        return JSONResponse(
            content=ResponseModel.error(message="Invalid month value")
        )
        # return {
        #     "status_code": 400,
        #     "message": "Invalid month value",
        # }
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
    
    current_user_id = current_user.id

    currentuser = db.query(User).get(current_user_id)
    if currentuser:
        currentuser.last_relapse_date = datetime.date.today()
        db.commit()
    else:
        currentuser = User(
            last_relapse_date=datetime.date.today(),
            id=current_user_id,
        )
        db.add(currentuser)
        db.commit()
    return JSONResponse(content=ResponseModel.success(data={"new_relapse_date": datetime.date.today().strftime("%Y-%m-%d")},
            message="relapse date updated"), status_code=status.HTTP_200_OK)


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

    Returns:
        {
            "status": "success",
            "message": "Relapses retrieved.",
            "data": [
                {
                "day": 1,
                "month": 12,
                "bottles_drank": 1,
                "month_id": 1,
                "id": 1,
                "year": 2022,
                "user": 1
                },
                {
                "day": 2,
                "month": 12,
                "bottles_drank": 1,
                "month_id": 1,
                "id": 2,
                "year": 2022,
                "user": 1
                },
                ...
            ]
        }

    Raises:
        HTTPException [424]: "message": "There are no relapse dates for this month and year"
        HTTPException [401]: Unauthorised

    """
    # relapses = relapse.get_multi_by_user(db=db, user_id=current_user.id, skip=skip, limit=limit)
    relapses = db.query(Relapse).filter(
        Relapse.user == current_user.id,
        Relapse.month == month,
        Relapse.year == year,
    ).all()

    if len(jsonable_encoder(relapses)) < 1:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={
                "message": "There are no relapse dates for this month and year"
                }
            )
    return JSONResponse(content=ResponseModel.success(data=jsonable_encoder(relapses), message="Relapses retrieved."), 
            status_code=status.HTTP_200_OK)


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
    Returns:

            {
                "status": "success",
                "message": "milestone retrieved",
                "data": {
                    "clean_days": 0,
                    "milestone": 1
                }
            }
    Raises:
            HTTPException [401]: Unauthorised
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

    return JSONResponse(content=ResponseModel.success(data=result, message="milestone retrieved"), status_code=status.HTTP_200_OK)


@router.get(
    "/leaderboard",
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
async def get_leaderboard(
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
    Returns:

            {
                "status": "success",
                "message": "summary retrieved",
                "data": {
                    "clean_days": 0,
                    "milestone": 1
                }
            }
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

    return JSONResponse(content=ResponseModel.success(data=result, message="summary retrieved"), status_code=status.HTTP_200_OK)


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
        {
            "status": "success",
            "message": "history list retrieved",
            "data": [
                {
                "title": "December 2022",
                "bottle_count": 4
                }
            ]
        } 
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

    return JSONResponse(content=ResponseModel.success(data=result, message="history list retrieved"), status_code=status.HTTP_200_OK)
