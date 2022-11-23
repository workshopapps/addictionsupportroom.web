import datetime
from api.example import schemas
from db.models import Example, Messages
from sqlalchemy import select
from sqlalchemy.orm import Session

from typing import (
    Any,
)
from .schemas import (
    MessageCreate,
)
from sqlalchemy.sql import (
    text,
)
import uuid
from api import deps


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


async def send_new_message(  # pylint: disable=R0911
    sender_id: int,
    request: MessageCreate,
    file: Any,
    room_id: int,
    session: Session,
):
    """
    A method to insert a new message into the messages table.

    Args:
        sender_id (int) : A user id that represents the sender of the message.
        request (MessageCreate) : A schema for the message.
        file (Any) : An image to upload to Deta drive.
        room_id (int) : the id of the room.
        session (AsyncSession) : SqlAlchemy session object.

    Returns:
        Result: Database result.
    """

    if not request.content:
        return {
            "status_code": 400,
            "message": "You can't send an empty message!",
        }
    receiver = await deps.find_existed_user(id=request.receiver, session=session)
    if not receiver:
        return {
            "status_code": 400,
            "message": "You can't send a message to a non existing" " user!",
        }
    if receiver.id == sender_id:
        return {
            "status_code": 400,
            "message": "You can't send a message to yourself!",
        }

    messages = Messages()
    messages.sender = sender_id
    messages.receiver = receiver.id
    messages.content = request.content
    messages.message_type = request.message_type
    messages.media = request.media
    messages.creation_date = datetime.datetime.utcnow()

    session.add(messages)
    session.commit()
    session.refresh(messages)

    # await session.execute(text(query), values)
    results = {
        "status_code": 201,
        "message": "A new message has been delivered successfully!",
        "data": messages,
    }
    return results
