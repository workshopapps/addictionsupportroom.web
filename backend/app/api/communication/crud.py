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
from api.auth.schemas import (
    UserObjectSchema,
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

async def get_sender_receiver_messages(
    sender: UserObjectSchema, receiver: str, session: Session
):
    print(receiver)
    print(sender.id)

    """
    A method to fetch messages between a sender and a receiver.

    Args:
        sender (UserObjectSchema) : A user object schema that contains infor about a sender.
        receiver (EmailStr) : An email for the recipient of the message.
        session (AsyncSession) : SqlAlchemy session object.

    Returns:
        Result: Database result.
    """
    receiver = await deps.find_existed_user(id=receiver, session=session)
    if not receiver:
        return {
            "status_code": 400,
            "message": "Contact not found!",
        }
    query = """
        SELECT
            id,
            content,
            CASE
                WHEN sender = :sender_id THEN "sent"
                WHEN receiver = :sender_id THEN "received"
                ELSE NULL
            END as type,
            media,
            creation_date
        FROM
            messages
        WHERE (
          sender = :sender_id
            AND
          receiver = :receiver_id
        )
        OR (
          sender = :receiver_id
            AND
          receiver = :sender_id
        )
        ORDER BY
          creation_date
    """
    values = {"sender_id": sender.id, "receiver_id": receiver.id}

    result = session.execute(text(query), values)
    messages_sent_received = result.fetchall()
    results = {
        "status_code": 200,
        "result": messages_sent_received,
    }
    # Mark received messages by this sender as read
    query = """
        UPDATE
          messages
        SET
          status = 0,
          modified_date = :modified_date
        WHERE
          sender = :receiver_id
        AND
          receiver = :sender_id
    """
    values = {
        "sender_id": sender.id,
        "receiver_id": receiver.id,
        "modified_date": datetime.datetime.utcnow(),
    }
    session.execute(text(query), values)
    return results

