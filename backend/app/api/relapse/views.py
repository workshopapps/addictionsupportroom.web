from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, OAuth2AuthorizationCodeBearer
from sqlalchemy.orm import Session
from db.models import Relapse
from api import deps
from .schemas import RelapseBase, RelapseCreate, RelapseInDB
from db.models import User

from .crud import relapse

router = APIRouter()

auth_scheme = HTTPBearer()
@router.post("/", response_model=RelapseInDB)
async def create_relapse(
    *, db: Session = Depends(deps.get_db), relapse_in: RelapseCreate,
    current_user: User = Depends(deps.get_current_user),
    token: OAuth2AuthorizationCodeBearer = Depends(auth_scheme)
    ) -> Any:
    """
    Create Relapse
    """
    new_relapse = relapse.create_with_user(db=db, obj_in=relapse_in, user_id=current_user.id)
    return new_relapse

@router.get("/", response_model=List[RelapseInDB])
async def read_relapses(
    db: Session = Depends(deps.get_db),  skip: int = 0,
    limit: int = 100, current_user: User = Depends(deps.get_current_user))-> Any:
    """
    Retrieve Relapse Days
    """
    relapses = relapse.get_multi_by_user(db=db, user_id=current_user.id, skip=skip, limit=limit)
    return relapses 
