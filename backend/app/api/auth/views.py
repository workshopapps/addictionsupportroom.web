from api.auth import schemas
from api.auth.schemas import UserLogin, AccessToken
from api.common.schemas import ResponseSchema, ResponseModel
from api.communication.schemas import RoomCreate
from db import models
import logging
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from api import deps
from api.communication import crud

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from deps import get_current_user

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/signup", response_model=schemas.UserOut)
async def signup(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):

    db_user = models.User()
    db_user.username = user.username
    db_user.avatar = user.avatar
    db_user.is_active = True
    db_user.hashed_password = deps.get_password_hash("general_password")

    try:
        # Create a new user
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        # Add user to General chatroom
        await create_assign_new_room_member(
            db_user.id,
            session=db,
            room_obj=RoomCreate(
                join=1,
                room_name='general',
                description='A General Chat room for all',
            ))

    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token to authorize user to access further endpoints
    access_token = deps.create_access_token(data={"sub": str(db_user.id)})
    user_out = schemas.UserOut(**db_user.__dict__, access_token=access_token)
    return user_out


async def create_assign_new_room_member(
    user_id: int,
    room_obj,
    session: Session,
):
    # Create a new room if it doesn't exist as a member

    room_obj.room_name = room_obj.room_name.lower()
    if not room_obj.room_name:
        results = {
            "status_code": 400,
            "message": "Make sure the room name is not empty!",
        }
        return results

    # Check if room already exists
    room = await crud.find_existed_room(room_obj.room_name, session)
    if not room:
        # Room doesn't exist: do this
        await crud.create_room(room_obj.room_name, room_obj.description,
                               session)

        logger.info(f"Creating room `{room_obj.room_name}`.")

    results = await crud.create_assign_new_room(user_id, room_obj, session)
    return results


@router.post(
    "/login",
    description=
    'Login with only a unique username, no password is needed for now',
    response_model=ResponseModel,
    responses={
        400:
        ResponseModel.sample(
            'Invalid Username.',
            ResponseModel.error('Invalid Username.'),
        ),
    },
)
async def login(request: UserLogin, db: Session = Depends(deps.get_db)):

    print(request)
    db_user = await deps.authenticate_user(
        request.username,
        'general-password',
        db,
    )
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token to authorize user to make further API
    access_token = deps.create_access_token(data={"sub": str(db_user.id)})

    user_out = schemas.UserOut(**db_user.__dict__, access_token=access_token)
    return ResponseModel.success(user_out, message='Successfully logged in')


# @router.post("/login")
# def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     # Check if user is in DB
#     user = authenticate_user(form_data.username, form_data.password, db)
#     if not user:
#         raise token_exception()

#     # Create token to authorize user to make further API
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={'sub': user.username}, expires_delta=access_token_expires)
#     return {"access_token": access_token, "token_type": "bearer"}
