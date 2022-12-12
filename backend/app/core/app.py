from api.router import api_router
from api.v2.router import api_router_v2
from api.v1.router import api_router_v1
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db.models import Base
from db.db import engine



def get_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="SoberPal Project",
        description="SoberPal API",
        version="1.0",
        docs_url="/api/docs/",
        redoc_url="/api/redoc/",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    #create and mount version 1 of soberpal API
    appv1 = FastAPI(
        title="SoberPal Project",
        description="SoberPal API",
        docs_url="/docs/",
        redoc_url="/redoc/",
        openapi_url="/openapi.json",
        default_response_class=UJSONResponse,
    )
    appv1.include_router(router=api_router_v1, prefix="/api")
    app.mount("/api/v1", appv1)



    #create and mount version 2 of soberpal API
    appv2 = FastAPI(
        title="Soberpal Project V2",
        description="Soberpal API V2",
        docs_url="/docs/",
        redoc_url="/redoc/",
        openapi_url="/openapi.json",
        default_response_class=UJSONResponse
    )

    appv2.include_router(router=api_router_v2, prefix="/api")
    app.mount("/api/v2", appv2)


    app.include_router(router=api_router, prefix="/api")

    return app
