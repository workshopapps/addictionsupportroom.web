from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from sqlalchemy.orm import Session
from api.common.schemas import ResponseSchema
from .schemas import GetAllContactsResults, RoomCreate, MessageCreateRoom

from fastapi import APIRouter, Depends


from api import deps
from typing import List
from .crud import (
    # delete_chat_messages,
    # get_chats_user,
    get_sender_receiver_messages,
    send_new_message,
    create_assign_new_room,
    get_room_conversations,
    get_rooms_user,
    send_new_room_message,
    get_user_contacts
)

from .schemas import (
    DeleteChatMessages,
    GetAllMessageResults,
    MessageCreate,
)

from api.auth.schemas import (
    UserBase,
)
from api.web_sockets.router import router as web_socket_router

router = APIRouter()

router.include_router(web_socket_router, tags=["WebSocket"])


from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

@router.get(
    "/contacts",
    response_model= GetAllContactsResults | ResponseSchema,
    status_code=200,
    name="contacts:get-all-user-contacts",
    responses={
        200: {
            "model": GetAllContactsResults,
            "description": "A list of contacts for each user.",
        },
        400: {
            "model": ResponseSchema,
            "description": "User not found.",
        },
    },
)
async def get_contacts_user(
    currentUser: UserBase = Depends(deps.get_current_user),
    session: Session = Depends(deps.get_db),
):
    """
    Get all contacts for an authenticated user.
    """
    results = await get_user_contacts(currentUser.id, session)
    return results


@router.post(
    "/message",
    response_model=ResponseSchema,
    status_code=201,
    name="chats:send-message",
    responses={
        201: {
            "model": ResponseSchema,
            "description": "Message has been delivered successfully!",
        },
        401: {
            "model": ResponseSchema,
            "description": "Empty message, non existing receiver!",
        },
    },
)
async def send_message(
    request: MessageCreate,
    currentUser: UserBase = Depends(deps.get_current_user),  # pylint: disable=C0103
    session: Session = Depends(deps.get_db),
):

    """
    The send_message endpoint.

    Args:
        request (MessageCreate) : A `MessageCreate` schema that contains info about the recipient.
        currentUser (UserObjectSchema): The authenticated user as the sender of the message.
        session (AsyncSession) : An autocommit sqlalchemy session object.

    Returns:
        ResponseSchema: return a response schema object.
    """

    # results = {
    #     "status_code": 201,
    #     "message": "A new message has been delivered successfully!",
    #     "data": currentUser,
    # }
    # return results
    results = await send_new_message(currentUser.id, request, None, None, session)
    return results


@router.get(
    "/conversation",
    response_model=ResponseSchema | GetAllMessageResults,
    status_code=200,
    name="chats:get-all-conversations",
    responses={
        200: {
            "model": GetAllMessageResults,
            "description": "Return a list of messages between two parties.",
        },
    },
)
async def get_conversation(
    receiver: str,
    currentUser: UserBase = Depends(deps.get_current_user),  # pylint: disable=C0103
    session: Session = Depends(deps.get_db),
):
    """
    The get_conversation endpoint.

    Args:
        receiver (user_id) : The recipient id.
        currentUser (UserObjectSchema): The authenticated user as the sender of the message.
        session (AsyncSession) : An autocommit sqlalchemy session object.

    Returns:
        ResponseSchema | GetAllMessageResults: return a list of messages between sender and receiver
    """

    # results = {
    #     "status_code": 201,
    #     "message": "A new message has been delivered successfully!",
    #     "data": currentUser,
    # }
    # return results
    results = await get_sender_receiver_messages(currentUser, receiver, session)
    return results


# @router.get("/chat/images/user/{user_id}/{uuid_val}")
# async def get_sent_user_chat_images(user_id: int, uuid_val: str):
#     """
#     The get_sent_user_chat_images endpoint.

#     Args:
#         user_id (id) : The id of the sender of the image.
#         uuid_val (str): A unique uuid generated upon upload.

#     Returns:
#         responses: return a response object for a given url(image).
#     """
#     try:
#         img = sent_images.get(f"/chat/images/user/{user_id}/{uuid_val}")
#         return responses.StreamingResponse(
#             img.iter_chunks(), media_type="image/png"
#         )
#     except Exception:  # pylint: disable=W0703
#         return {"status_code": 400, "message": "Something went wrong!"}


@router.post(
    "/room",
    status_code=200,
    name="room:create-join",
    responses={
        200: {
            "model": ResponseSchema,
            "description": "Return a message that indicates a user has"
            " joined the room.",
        },
        400: {
            "model": ResponseSchema,
            "description": "Return a message that indicates if a user"
            " has already"
            " joined a room ",
        },
    },
)
async def create_room(
    room: RoomCreate,
    currentUser: UserBase = Depends(deps.get_current_user),
    session: Session = Depends(deps.get_db),
):
    """
    Create or join a room.
    """
    results = await create_assign_new_room(currentUser.id, room, session)
    return results


@router.get("/room/conversation", name="room:get-conversations")
async def get_room_users_conversation(
    room: str,
    currentUser: UserBase = Depends(deps.get_current_user),
    session: Session = Depends(deps.get_db),
):
    """
    Get Room by room name
    """
    results = await get_room_conversations(room, currentUser.id, session)
    return results


@router.post("/room/message", name="room:send-text-message")
async def send_room_message(
    request: MessageCreateRoom,
    currentUser: UserBase = Depends(deps.get_current_user),
    session: Session = Depends(deps.get_db),
):
    """
    Send a new message.
    """
    results = await send_new_room_message(currentUser.id, request, None, session)
    return results


@router.get("/rooms", status_code=200, name="rooms:get-rooms-for-user")
async def get_rooms_for_user(
    currentUser: UserBase = Depends(deps.get_current_user),
    session: Session = Depends(deps.get_db),
):
    """
    Fetch all the joined room for an authenticated user.
    """
    results = await get_rooms_user(currentUser.id, session)
    return results
