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
from api.relapse.views import router as relapse_router


api_router = APIRouter()
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
#api_router.include_router(relapse_router, prefix="/relapse", tags=["relapse"])