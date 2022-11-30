from fastapi import APIRouter, Depends, WebSocket
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import deps
from db.models import User
from .agora import Agora

router = APIRouter()

class Call(BaseModel):
    caller_username: str
    callee_username: str


@router.post("/")
def joinCall(data: Call, db: Session = Depends(deps.get_db)):
    #returns an agora token, channel name, caller username, and callee username for joining a call room
    agora = Agora()

    channelName = data.caller_username + data.callee_username

    token = agora.generate_token(channelName)

    return {
        "token": token,
        "caller": data.caller_username,
        "callee": data.callee_username,
        "channelName": channelName
    }


@router.websocket("/callws")
async def call_socket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({
                                    "status": "connected"
                                })
    while True:        
        await websocket.receive_json()