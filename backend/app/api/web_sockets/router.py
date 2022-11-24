import asyncio
from fastapi import (
    APIRouter,
    Depends,
)
from aioredis import (
    from_url,
)

from fastapi.responses import HTMLResponse

from fastapi.websockets import (
    WebSocket,
)
import logging
from sqlalchemy.orm import Session
from api import deps
from core import settings

from api.auth.schemas import (
    UserObjectSchema,
)

# from app.utils.dependencies import (
#     get_db_autocommit_session_socket,
# )
from api.utils.pub_sub_handlers import (
    consumer_handler,
    producer_handler,
)

async def redis_conn() -> str:
    """
    Assemble Redis URL from self.

    Args:
        self ( _obj_ ) : object reference.

    Returns:
        str: The assembled Redis host URL.
    """
    print(settings.settings.REDIS_PASSWORD)
    print(settings.settings.REDIS_USERNAME)

    return await from_url(
        "redis://"
        + settings.settings.REDIS_USERNAME
        + ":"
        + settings.settings.REDIS_PASSWORD
        + "@"
        + settings.settings.REDIS_HOST
        + ":"
        + settings.settings.REDIS_PORT
        + "/"
        "0",
        decode_responses=True,
    )

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# @router.websocket("/ws")
# ws://0.0.0.0:8000/api/chat/ws

# @router.websocket("/ws/room/{sender_id}/{room_name}")
# async def websocket_room_endpoint(
#     websocket: WebSocket,
#     sender_id: int,
#     room_name: str,
#     session: AsyncSession = Depends(get_db_autocommit_session_socket),
# ):
#     try:
#         # add user
#         # the user on the
#         await websocket.accept()
#         conn = await settings.redis_conn()
#         pubsub = conn.pubsub()

#         consumer_task = consumer_handler(
#             connection=conn,
#             topic=room_name,
#             web_socket=websocket,
#             sender_id=sender_id,
#             receiver_id=None,
#             session=session,
#         )
#         producer_task = producer_handler(
#             pub_sub=pubsub, topic=room_name, web_socket=websocket
#         )
#         done, pending = await asyncio.wait(
#             [consumer_task, producer_task],
#             return_when=asyncio.FIRST_COMPLETED,
#         )
#         logger.debug(f"Done task: {done}")
#         for task in pending:
#             logger.debug(f"Canceling task: {task}")
#             task.cancel()

#     except Exception as ex:
#         message = f"An exception of type {type(ex).__name__} occurred. Arguments:\n{ex.args!r}"  # noqa: E501
#         logger.error(message)
#         logger.warning("Disconnecting Websocket")
#         await websocket.close()
#         if conn:
#             await conn.close()
#             del conn

# ws://localhost:8000/ws
@router.websocket("/ws/chat/{sender_id}/{receiver_id}")
async def websocket_contact_chat_endpoint(
    websocket: WebSocket,
    sender_id: int,
    receiver_id: int,
    session: Session = Depends(deps.get_db),
):
    try:
        sorted_chat = sorted([sender_id, receiver_id])
        await websocket.accept()
        conn = await redis_conn()
        pubsub = conn.pubsub()
        consumer_task = consumer_handler(
            connection=conn,
            topic="_".join(map(lambda val: str(val), sorted_chat)),
            web_socket=websocket,
            sender_id=sender_id,
            receiver_id=receiver_id,
            session=session,
        )
        producer_task = producer_handler(
            pub_sub=pubsub,
            topic="_".join(map(lambda val: str(val), sorted_chat)),
            web_socket=websocket,
        )
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        logger.debug(f"Done task: {done}")
        for task in pending:
            logger.debug(f"Canceling task: {task}")
            task.cancel()

    except Exception as ex:
        message = f"An exception of type {type(ex).__name__} occurred. Arguments:\n{ex.args!r}"  # noqa: E501
        logger.error(message)
        logger.warning("Disconnecting Websocket")
        await websocket.close()
        if conn:
            await conn.close()
            del conn
