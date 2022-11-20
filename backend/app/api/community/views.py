from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from sqlalchemy.orm import Session
from db.models import Example
from fastapi import APIRouter, Depends

from api import deps

router = APIRouter()


@router.get("/call/")
async def get_channel_id(
    db: Session = Depends(deps.get_db),
):
    return {'channel_id': '7917adbcba3f47bf802b3824ad96b8a8'}


# @router.get("/", response_model=list[ExampleSchema])
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
