from api.example import schemas
from db.db import db_session
from db.models import Example
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ExampleService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def get_all_examples(self) -> list[schemas.Examples]:
        examples = await self.session.execute(select(schemas.Examples))

        return examples.scalars().fetchall()

    async def create_example(self, data: schemas.Examples) -> Example:
        example = Example(**data.dict())
        # self.session.add(example)
        # await self.session.commit()
        # await self.session.refresh(example)

        return example
