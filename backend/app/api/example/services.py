from api.example import schemas
from db.models import Example
from sqlalchemy import select
from sqlalchemy.orm import Session


class ExampleService:
    # def __init__(self, session: AsyncSession = Depends(db_session)):
    #     self.session = session

    async def get_all_examples(self, db: Session) -> list[schemas.Examples]:
        examples = db.query(Example).all()

        return examples

    def create_example(self, db: Session, data) -> Example:
        example = Example(**data.dict())
        db.add(example)
        db.commit()
        db.refresh(example)

        return example
