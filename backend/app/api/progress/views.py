from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from api.common.schemas import ResponseSchema
from api.auth.schemas import UserBase
from . import services
from sqlalchemy.orm import Session
from db.models import Month, User, Streak
from fastapi import APIRouter, Depends
from . import schemas
from sqlalchemy.orm import Session
import datetime
from .schemas import GetAllHistoryResult
from typing import Any
from fastapi.encoders import jsonable_encoder

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







@router.get("/leaderboard/total_clean_days", response_model=schemas.TotalCleanDays)
def get_current_user_streak(*,
                        db: Session = Depends(deps.get_db),
                        current_user: User = Depends(deps.get_current_user)) -> Any:
    streak = services.get_auser_total_clean_days(db=db, current_user_id=current_user.id)
    return streak