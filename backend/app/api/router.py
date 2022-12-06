from fastapi.routing import APIRouter

# from api.system.views import router as system_router
from api.auth.views import router as auth_router
from api.communication.views import router as communication_router
from api.community.views import router as community_router
from api.contact_us.views import router as contact_router
from api.home.routers import router as home_router
from api.example.views import router as example_router
from api.progress.views import router as progress_router
from api.call.views import router as call_router
# from api.relapse.views import router as relapse_router
from api.blog.views import router as blog_router

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from api.auth.views import login
from api import deps
from api.auth.schemas import UserLogin

api_router = APIRouter()


@api_router.post("/docs/token", include_in_schema=False)
async def token(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(deps.get_db)):
    """
    The an endpoint for quick login from the documentation 

    Returns:
        UserOut: return a UserOut schema with a token object.
    """

    val = await login(UserLogin(username=form_data.username), db=db)

    return {"access_token": val['token'], "token_type": "bearer"}


api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(home_router, prefix="/home", tags=["Home"])
api_router.include_router(community_router,
                          prefix="/community",
                          tags=["Community"])
api_router.include_router(communication_router,
                          prefix="/communication",
                          tags=["Communication"])
api_router.include_router(call_router, prefix="/call", tags=["Call"])
api_router.include_router(progress_router,
                          prefix="/progress",
                          tags=["Progress"])
api_router.include_router(contact_router, prefix="/contact", tags=["Contact"])
# api_router.include_router(relapse_router, prefix="/relapse", tags=["relapse"])
api_router.include_router(blog_router, prefix="/blog", tags=["Blog"])
