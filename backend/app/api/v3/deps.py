from datetime import datetime, timedelta
from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
# from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from .auth.schemas import UserBase, AccessToken

from db import models
from db.db import SessionLocal
from jose import jwt, JWTError
# from app.core.config import settings
# from app.db.session import SessionLocal

# reusable_oauth2 = OAuth2PasswordBearer(
#     tokenUrl=f"{settings.API_V1_STR}/login/access-token"
# )
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

# SECRET_KEY = "Kffdjkfskjdnsjdkjsdnksjjkdnkjskjd"
SECRET_KEY = "Pr4aIQapyXbC2bgApiLZTNRbgPB1nd15"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def find_existed_user(id: int, db: Session = Depends(get_db)) -> UserBase:
    """
    A method to fetch a user info given an ID.
    Args:
        ID (Str) : A given user ID.
        session (AsyncSession) : SqlAlchemy session object.
    Returns:
        Dict[str, Any]: a dict object that contains info about a user.
    """

    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return UserBase(**user.__dict__)

    return user


async def find_existed_user_by_username_and_password(username: str,
                                        password: str,
                                        session: Session) -> UserBase:
    """
    A method to fetch a user info given an username.
    Args:
        username (Str) : A given user username.
        session (AsyncSession) : SqlAlchemy session object.
    Returns:
        Dict[str, Any]: a dict object that contains info about a user.
    """

    user = session.query(
        models.User).filter(models.User.username == username).first()
    if user:
        if verify_password(password, user.hashed_password):
            return UserBase(**user.__dict__)


def get_user(db, username: str):
    user: models.User = db.query(
        models.User).filter(models.User.username == username).first()

    return user


def authenticate_user(username, password, db):
    # get user by username and password
    user = find_existed_user_by_username_and_password(session=db, username=username, password=password)

    if not user:
        return False

    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    expire = datetime.utcnow() + access_token_expires

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return AccessToken(token=encoded_jwt, token_type='bearer')


def get_current_user(token: str, db: Session = Depends(get_db)):

    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("sub")
        if id is None:
            raise get_user_exception()
        

        user = find_existed_user(id=id, db=db)

        if not user:
            raise get_user_exception()

        return int(id)
        
    except (JWTError, ValidationError):
        raise get_user_exception()


# def get_current_active_user(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_active(current_user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

# def get_current_active_superuser(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(
#             status_code=400, detail="The user doesn't have enough privileges"
#         )
#     return current_user


def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User not authorized",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception