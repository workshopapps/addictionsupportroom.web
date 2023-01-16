from api.v3.router import api_router_v3
from api.v2.router import api_router_v2
from api.v1.router import api_router_v1
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db.models import Base
from db.db import engine


def get_app() -> FastAPI:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI()

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
        version="1.0",
        redoc_url="/redoc/",
        openapi_url="/open.json",
        default_response_class=UJSONResponse
    )
    appv1.include_router(router=api_router_v1)
    app.mount("/api/v1", appv1)

    #create and mount version 2 of soberpal API
    appv2 = FastAPI(title="Soberpal Project V2",
                    description="Soberpal API V2",
                    version="2.0",
                    docs_url="/docs/",
                    redoc_url="/redoc/",
                    openapi_url="/open.json",
                    default_response_class=UJSONResponse
                )

    appv2.include_router(router=api_router_v2)
    app.mount("/api/v2", appv2)

    #create and mount version 3 of soberpal API
    appv3 = FastAPI(title="Soberpal Project V3",
                    description="Soberpal API V3",
                    version="3.0",
                    docs_url="/docs/",
                    redoc_url="/redoc/",
                    openapi_url="/open.json",
                    default_response_class=UJSONResponse
                )
    appv3.include_router(router=api_router_v3)
    app.mount("/api/v3", appv3)

    return app
