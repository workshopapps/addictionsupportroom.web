from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, OAuth2AuthorizationCodeBearer
from sqlalchemy.orm import Session
from db.models import Relapse
from api import deps
from .schemas import RelapseBase, RelapseCreate, RelapseInDB
from db.models import User

from .crud import relapse, create_relapse_with_user

router = APIRouter()

auth_scheme = HTTPBearer()
@router.post("/")
async def create_relapse(
    *, db: Session = Depends(deps.get_db), relapse_in: RelapseCreate,
    current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme)
    ) -> Any:
    """
    Create Relapse
    """
    print(current_user)
    # new_relapse = relapse.create_with_user(db=db, obj_in=relapse_in, user_id=current_user.id)
    new_relapse = create_relapse_with_user(db=db, user_id=current_user.id, relapse=relapse_in)
    return new_relapse

@router.get("/")
async def read_relapses(*,
    db: Session = Depends(deps.get_db),  skip: int = 0,
    limit: int = 100, current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme))-> Any:
    """
    Retrieve Relapse Days
    """
    print(current_user)
    # relapses = relapse.get_multi_by_user(db=db, user_id=current_user.id, skip=skip, limit=limit)
    relapses = db.query(Relapse).filter(Relapse.user==current_user.id).all()
    return relapses 
