import datetime
import logging
from api.example import schemas
from db.models import Example, Messages, Rooms
from sqlalchemy import select
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

from typing import (
    Any,
)

from .schemas import (
    MessageCreate,
    MessageCreateRoom,
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


# ----------------------------------------------------------------
# Rooms
# ----------------------------------------------------------------
async def create_assign_new_room(user_id: int, room_obj, session: Session):
    room_obj.room_name = room_obj.room_name.lower()
    if not room_obj.room_name:
        results = {
            "status_code": 400,
            "message": "Make sure the room name is not empty!",
        }
        return results
    room = await find_existed_room(room_obj.room_name, session)
    if not room:
        if room_obj.join == 0:
            await create_room(room_obj.room_name, room_obj.description, session)
        else:
            return {
                "status_code": 400,
                "message": "Room not found!",
            }
        logger.info(f"Creating room `{room_obj.room_name}`.")
        room = await find_existed_room(room_obj.room_name, session)
        user = await find_existed_user_in_room(user_id, room.id, session)
        if user:
            logger.info(f"`{user_id}` has already joined this room!")
            results = {
                "status_code": 400,
                "message": "You have already joined room" f"{room_obj.room_name}!",
            }
        else:
            await join_room(user_id, room.id, session, True)
            logger.info(f"Adding {user_id} to room `{room_obj.room_name}` as a member.")
            results = {
                "status_code": 200,
                "message": f"You have joined room {room_obj.room_name}!",
            }
        return results

    else:
        user = await find_existed_user_in_room(user_id, room.id, session)
        if user and room_obj.join == 1:
            if user.banned == 1:
                logger.info(f"`{user_id}` can't join this room!")
                results = {
                    "status_code": 400,
                    "message": "You have been banned from this room.",
                }
            else:
                logger.info(f"`{user_id}` has already joined this room!")
                results = {
                    "status_code": 400,
                    "message": "You have already joined room" f"{room_obj.room_name}!",
                }
        elif not user and room_obj.join == 1:
            await join_room(user_id, room.id, session)
            logger.info(f"Adding {user_id} to room `{room_obj.room_name}` as a member.")
            results = {
                "status_code": 200,
                "message": f"You have joined room {room_obj.room_name}!",
            }
        else:
            logger.info("This room already exists.")
            results = {
                "status_code": 400,
                "message": "This room already exists. Join it, perhaps?",
            }
        return results


async def find_existed_room(room_name: str, session: Session):
    query = """
        SELECT
          *
        FROM
          rooms
        WHERE
          room_name = :room_name
    """
    values = {"room_name": room_name}

    result = session.execute(text(query), values)
    return result.fetchone()


async def find_existed_user_in_room(user_id: int, room_id: int, session: Session):
    query = """
        SELECT
          *
        FROM
          room_members
        WHERE
          room = :room_id
        AND
          member = :user_id
    """
    values = {"room_id": room_id, "user_id": user_id}

    result = session.execute(text(query), values)
    return result.fetchone()


async def find_admin_in_room(user_id: int, room_id: int, session: Session):
    query = """
        SELECT
          *
        FROM
          room_members
        WHERE
          room = :room_id
        AND
          member = :user_id
        AND
          admin = 1
    """
    values = {"room_id": room_id, "user_id": user_id}

    result = session.execute(text(query), values)
    return result.fetchone()


async def create_room(room_name: int, description: str, session: Session):
    query = """
        INSERT INTO rooms (
          room_name,
          description,
          creation_date
        )
        VALUES (
          :room_name,
          :description,
          :creation_date
        )
    """
    values = {
        "room_name": room_name,
        "description": description,
        "creation_date": datetime.datetime.utcnow(),
    }

    print(room_name, description)

    room = Rooms()
    room.room_name = room_name
    room.description = description

    session.add(room)
    session.commit()
    session.refresh(room)
    return room


async def join_room(user_id: int, room_id: int, session: Session, is_admin=False):
    if is_admin:
        query = """
            INSERT INTO room_members (
              room,
              member,
              banned,
              admin,
              creation_date
            )
            VALUES (
              :room,
              :member,
              0,
              1,
              :creation_date
            )
        """
    else:
        query = """
            INSERT INTO room_members (
              room,
              member,
              banned,
              admin,
              creation_date
            )
            VALUES (
              :room,
              :member,
              0,
              0,
              :creation_date
            )
        """
    values = {
        "room": room_id,
        "member": user_id,
        "creation_date": datetime.datetime.utcnow(),
    }

    return session.execute(text(query), values)


async def get_room_conversations(room_name: str, sender_id: int, session: Session):
    room = await find_existed_room(room_name, session)
    if not room:
        return {
            "status_code": 400,
            "message": "Room not found!",
        }
    # test if sender_id is admin
    admin = await find_admin_in_room(sender_id, room.id, session)
    if admin:
        query = """
            SELECT
                messages.id as msg_id,
                messages.content,
                CASE
                    WHEN messages.sender = :sender_id THEN "sent"
                    ELSE "received"
                END as type,
                messages.media,
                messages.creation_date,
                users.id as id,
                users.first_name,
                users.last_name,
                users.bio,
                users.chat_status,
                users.email,
                users.phone_number,
                users.profile_picture,
                room_members.admin
            FROM
                messages
            LEFT JOIN
                users
            ON
              messages.sender = users.id
            LEFT JOIN
                room_members
            ON
              messages.room = room_members.room
            WHERE
              messages.room = :room_id
            GROUP BY
              messages.id
            ORDER BY
              messages.creation_date
        """
    else:
        query = """
            SELECT
                messages.id as msg_id,
                messages.content,
                CASE
                    WHEN messages.sender = :sender_id THEN "sent"
                    ELSE "received"
                END as type,
                messages.media,
                messages.creation_date,
                users.id as id,
                users.first_name,
                users.last_name,
                users.bio,
                users.chat_status,
                users.email,
                users.phone_number,
                users.profile_picture
            FROM
                messages
            LEFT JOIN
                users
            ON
              messages.sender = users.id
            WHERE
              messages.room = :room_id
            ORDER BY
              messages.creation_date
        """
    values = {"room_id": room.id, "sender_id": sender_id}
    result = session.execute(text(query), values)
    messages_sent_received = result.fetchall()
    results = {
        "status_code": 200,
        "result": messages_sent_received,
    }
    return results


async def send_new_room_message(
    sender_id: int,
    request: MessageCreateRoom,
    bin_photo: str,
    session: Session,
):
    # Check for empty message
    if not request.content and not bin_photo:
        return {
            "status_code": 400,
            "message": "You can't send an empty message!",
        }
    room = await find_existed_room(request.room, session)
    print(room)
    if not room:
        return {
            "status_code": 400,
            "message": "You can't send a message to a non existing room!",
        }
    user = await find_existed_user_in_room(sender_id, room.id, session)
    if not user:
        logger.info("Can't send a message to this room!")
        results = {
            "status_code": 400,
            "message": "You can't send a message to a room you" " have not joined yet.",
        }
    else:
        # create a new message
        if request.media:
            results = await send_new_message(
                sender_id, request, bin_photo, room.id, session
            )
        else:
            results = await send_new_message(sender_id, request, None, room.id, session)
    return results


async def get_rooms_user(user_id: int, session: Session):
    # get all rooms for this user.
    query = """
        SELECT
          *
        FROM
          room_members
        LEFT JOIN
          rooms
        ON
          room_members.room= rooms.id
        WHERE
          room_members.member= :user_id
        AND
          room_members.banned= 0
    """
    values = {"user_id": user_id}

    result = await session.execute(text(query), values)
    contacts = result.fetchall()
    results = {"status_code": 200, "result": contacts}
    return results
