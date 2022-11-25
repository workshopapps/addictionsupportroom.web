from datetime import timedelta
from sqlite3 import IntegrityError
from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from api.auth import schemas
from db import models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from api import deps
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):

    db_user = models.User()
    db_user.username = user.username
    db_user.avatar = user.avatar
    db_user.is_active = True
    db_user.hashed_password = deps.get_password_hash("general_password")

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token to authorize user to make further API
    access_token = deps.create_access_token(data={"sub": str(db_user.id)})
    user_out = schemas.UserOut(**db_user.__dict__, access_token=access_token)
    return user_out


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(deps.get_db)):

    db_user = await deps.authenticate_user(form_data.username,
                                           form_data.password, db)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token to authorize user to make further API
    access_token = deps.create_access_token(data={"sub": str(db_user.id)})
    user_out = schemas.UserOut(**db_user.__dict__, access_token=access_token)

    return user_out


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
