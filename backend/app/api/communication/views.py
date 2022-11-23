from api.example.schemas import Examples, ExampleSchema
from api.example.services import ExampleService
from sqlalchemy.orm import Session
from api.common.schemas import ResponseSchema
from db.models import Example, Base
from db.db import engine
from fastapi import APIRouter, Depends


from api import deps
from typing import List
from .crud import (
    # delete_chat_messages,
    # get_chats_user,
    # get_sender_receiver_messages,
    send_new_message,
)

from .schemas import (
    DeleteChatMessages,
    GetAllMessageResults,
    MessageCreate,
)

from api.auth.schemas import (
    UserObjectSchema,
)

router = APIRouter()

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse


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
    currentUser: UserObjectSchema = Depends(
        deps.get_current_user
    ),  # pylint: disable=C0103
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


# @router.get(
#     "/conversation",
#     response_model=Union[ResponseSchema, GetAllMessageResults],
#     status_code=200,
#     name="chats:get-all-conversations",
#     responses={
#         200: {
#             "model": GetAllMessageResults,
#             "description": "Return a list of messages between two parties.",
#         },
#     },
# )


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/api/communication/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get("/web")
async def get():
    return HTMLResponse(html)


# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


@router.get("/", response_model=list[ExampleSchema])
async def get_examples(
    db: Session = Depends(deps.get_db),
) -> list[Example]:
    example_service = ExampleService()
    return await example_service.get_all_examples(db=db)


@router.post("/", response_model=ExampleSchema)
async def create_example(
    data: Examples,
    db: Session = Depends(deps.get_db),
) -> Example:
    example_service = ExampleService()
    example = example_service.create_example(db=db, data=data)
    return example
