from fastapi.routing import APIRouter

from api.v2.auth.views import router as auth_router
from api.v2.communication.views import router as communication_router
from api.v2.community.views import router as community_router
from api.v2.contact_us.views import router as contact_router
from api.v2.home.routers import router as home_router
from api.v2.example.views import router as example_router
from api.v2.progress.views import router as progress_router
from api.v2.call.views import router as call_router
from api.v2.blog.views import router as blog_router
from api.v2.emergency.views import router as emergency_router
from api.v2.forum.views import router as forum_router
from api.v2.feedback.views import router as feedback_router
from api.v2.settings.views import router as settings_router


from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from api.v2.auth.views import login
from api.v2 import deps
from api.v2.auth.schemas import UserLogin

api_router_v2 = APIRouter()


@api_router_v2.post("/docs/token", include_in_schema=False)
async def token(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(deps.get_db)):
    """
    The an endpoint for quick login from the documentation 

    Returns:
        UserOut: return a UserOut schema with a token object.
    """

    val = await login(UserLogin(username=form_data.username), db=db)

    access_token = val['data']['access_token']

    return {"access_token": access_token['token'], "token_type": "bearer"}


api_router_v2.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router_v2.include_router(home_router, prefix="/home", tags=["Home"])
api_router_v2.include_router(community_router,
                          prefix="/community",
                          tags=["Community"])
api_router_v2.include_router(communication_router,
                          prefix="/communication",
                          tags=["Communication"])
api_router_v2.include_router(call_router, prefix="/call", tags=["Call"])
api_router_v2.include_router(progress_router,
                          prefix="/progress",
                          tags=["Progress"])
api_router_v2.include_router(contact_router, prefix="/contact", tags=["Contact"])
api_router_v2.include_router(blog_router, prefix="/blog", tags=["Blog"])
api_router_v2.include_router(emergency_router,
                          prefix="/emergency",
                          tags=["Emergency"])
api_router_v2.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])
api_router_v2.include_router(forum_router, prefix="/forum", tags=["Forum"])
api_router_v2.include_router(settings_router, prefix="/settings", tags=["Settings"])

api_router_v2.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])
