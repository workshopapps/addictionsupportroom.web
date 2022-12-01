from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from api.common.schemas import ResponseSchema
from api.auth.schemas import UserBase
from . import services
from sqlalchemy.orm import Session
from db.models import Month
from fastapi import APIRouter, Depends
from . import schemas
from sqlalchemy.orm import Session
import datetime
from .schemas import GetAllHistoryResult


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


# @router.post(
#     "/message",
#     response_model=ResponseSchema,
#     status_code=201,
#     name="chats:send-message",
#     responses={
#         201: {
#             "model": ResponseSchema,
#             "description": "Message has been delivered successfully!",
#         },
#         401: {
#             "model": ResponseSchema,
#             "description": "Empty message, non existing receiver!",
#         },
#     },
# )
# async def send_message(
#         request: MessageCreate,
#         currentUser: UserBase = Depends(deps.get_current_user),  # pylint: disable=C0103
#         session: Session = Depends(deps.get_db),
# ):
#     """
#     The send_message endpoint.

#     Args:
#         request (MessageCreate) : A `MessageCreate` schema that contains info about the recipient.
#         currentUser (UserObjectSchema): The authenticated user as the sender of the message.
#         session (AsyncSession) : An autocommit sqlalchemy session object.

#     Returns:
#         ResponseSchema: return a response schema object.
#     """

#     # results = {
#     #     "status_code": 201,
#     #     "message": "A new message has been delivered successfully!",
#     #     "data": currentUser,
#     # }
#     # return results
#     results = await send_new_message(currentUser.id, request, None, None,
#                                      session)
#     return results


@router.get("/leaderboard", response_model=list[schemas.Ranking])
def get_all_streaks(db: Session = Depends(deps.get_db)):
    ranks = services.get_all_users_streak(db=db)
    return ranks


@router.get("/leaderboard/top", response_model=list[schemas.Ranking])
def get_top_ranking(db: Session = Depends(deps.get_db)):
    top_ranks = services.get_top_20_users_with_high_streaks(db=db)
    return top_ranks


@router.get("/leaderboard/total_clean_days/{streak_id}",
            response_model=schemas.Ranking)
def get_specific_streak(streak_id: int, db: Session = Depends(deps.get_db)):
    streak = services.get_auser_total_clean_days(db=db, streak_id=streak_id)
    return streak


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