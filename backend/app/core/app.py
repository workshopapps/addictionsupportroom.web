from api.router import api_router
from fastapi import FastAPI
from fastapi.responses import UJSONResponse

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
        title="FastAPI Starter Project",
        description="FastAPI Starter Project",
        version="1.0",
        docs_url="/api/docs/",
        redoc_url="/api/redoc/",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.include_router(router=api_router, prefix="/api")

    return app
