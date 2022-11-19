from api.progress import schemas
from db.models.progress import Day
from db.db import db_session
from db.models.example import Example
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ProgressService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def get_all_examples(self) -> list[Example]:
        examples = await self.session.execute(select(Example))

        return examples.scalars().fetchall()

    async def create_example(self, data: schemas.DayCreate) -> Example:
        example = Example(**data.dict())
        self.session.add(example)
        await self.session.commit()
        await self.session.refresh(example)

        return example

    async def mark_a_day(self, data: schemas.Day):
        day = Day(**data.dict())

        self.session.add(day)
        await self.session.commit()
        await self.session.refresh(day)

        return day
