from datetime import timedelta
from sqlite3 import IntegrityError
from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from api.auth import schemas
from db import models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from api import deps

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
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token to authorize user to make further API
    access_token = deps.create_access_token(data={"sub": str(db_user.id)})
    user_out = schemas.UserOut(**user.dict(), access_token=access_token)
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

# @router.get("/signup", response_model=list[ExampleSchema])
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
