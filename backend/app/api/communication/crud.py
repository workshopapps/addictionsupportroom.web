import datetime
import logging
from api.example import schemas
from db.models import Example, Messages, Rooms, RoomMembers
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
    message = Messages()
    # if request.message_type == "media":  # pylint: disable=R1705
    #     pass
    #     if not room_id:
    #         if not request.media["preview"]:
    #             return {
    #                 "status_code": 400,
    #                 "message": "You can't upload an empty file!",
    #             }
    #         receiver = await find_existed_user(email=request.receiver, session=session)
    #         file_name = (
    #             f"/chat/images/user/{str(sender_id)}/image_{str(uuid.uuid4())}.png"
    #         )
    #         images.put(file_name, file)
    #         # create a new message
    #         query = """
    #             INSERT INTO messages (
    #               sender,
    #               receiver,
    #               content,
    #               message_type,
    #               media,
    #               status,
    #               creation_date
    #             )
    #             VALUES (
    #               :sender,
    #               :receiver,
    #               :content,
    #               :message_type,
    #               :media,
    #               1,
    #               :creation_date
    #             )
    #         """
    #         values = {
    #             "sender": sender_id,
    #             "receiver": receiver.id,
    #             "content": request.content,
    #             "message_type": request.message_type,
    #             "media": file_name,
    #             "creation_date": datetime.datetime.utcnow(),
    #         }
    #     else:
    #         if not request.media["preview"]:
    #             return {
    #                 "status_code": 400,
    #                 "message": "You can't upload an empty file!",
    #             }
    #         room = await find_existed_room(room_name=request.room, session=session)
    #         file_name = (
    #             f"/chat/images/room/{str(sender_id)}/image_{str(uuid.uuid4())}.png"
    #         )
    #         images.put(file_name, file)
    #         # create a new message
    #         query = """
    #             INSERT INTO messages (
    #               sender,
    #               room,
    #               content,
    #               message_type,
    #               media,
    #               status,
    #               creation_date
    #             )
    #             VALUES (
    #               :sender,
    #               :room,
    #               :content,
    #               :message_type,
    #               :media,
    #               1,
    #               :creation_date
    #             )
    #         """
    #         values = {
    #             "sender": sender_id,
    #             "room": room.id,
    #             "content": request.content,
    #             "message_type": request.message_type,
    #             "media": file_name,
    #             "creation_date": datetime.datetime.utcnow(),
    #         }
    #     await session.execute(text(query), values)
    #     return file_name
    # else:
    if not room_id:
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
        message.sender = sender_id
        message.receiver = receiver.id
        message.content = request.content
        message.status = 1
        message.message_type = request.message_type
        message.media = request.media
        message.creation_date = datetime.datetime.utcnow()

    else:
        message.sender = sender_id
        message.room = room_id
        message.content = request.content
        message.status = 1
        message.message_type = request.message_type
        message.media = request.media
        message.creation_date = datetime.datetime.utcnow()

    session.add(message)
    session.commit()
    session.refresh(message)

    results = {
        "status_code": 201,
        "message": "A new message has been delivered successfully!",
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
        receiver (user_id) : An id for the recipient of the message.
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
            END as status,
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
    # Check if room already exists
    room = await find_existed_room(room_obj.room_name, session)
    if not room:
        # Room doesn't exist: do this
        if room_obj.join == 0:
            # User wants to join a room, so create a new one
            await create_room(room_obj.room_name, room_obj.description, session)
        else:
            # User doesn't want to join whatever room
            return {
                "status_code": 400,
                "message": "Room not found!",
            }
        logger.info(f"Creating room `{room_obj.room_name}`.")
        room = await find_existed_room(room_obj.room_name, session)
        user = await find_existed_user_in_room(user_id, room.id, session)
        # Check if user is in newly created room
        if user:
            logger.info(f"`{user_id}` has already joined this room!")
            results = {
                "status_code": 400,
                "message": "You have already joined room" f"{room_obj.room_name}!",
            }
        else:
            # Join the room
            await join_room(user_id, room.id, session, True)
            logger.info(f"Adding {user_id} to room `{room_obj.room_name}` as a member.")
            results = {
                "status_code": 200,
                "message": f"You have joined room {room_obj.room_name}!",
            }
        return results

    else:
        # Room already exists: Check if User is in room
        user = await find_existed_user_in_room(user_id, room.id, session)
        print(user)
        if user and room_obj.join == 1:
            # If user was already in the room
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
            # If user was never in the room
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

    roommembers = RoomMembers()
    roommembers.room = room_id
    roommembers.member = user_id
    roommembers.banned = 0
    if is_admin:
        roommembers.admin = 1
    else:
        roommembers.admin = 0

    session.add(roommembers)
    session.commit()
    session.refresh(roommembers)

    return roommembers


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
                END as status,
                messages.media,
                messages.creation_date,
                users.id as id,
                users.username,
                users.avatar,
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
                END as status,
                messages.media,
                messages.creation_date,
                users.id as id,
                users.username,
                users.avatar
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
