#imports
from fastapi import APIRouter, Depends, WebSocket, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import deps
from db.models import User
from .agora import Agora
from typing import List
import json
from .notify import NotificationManager



#router instance
router = APIRouter()

#notification manager class instance
notify = NotificationManager()



#expected Base Models

class MakeCall(BaseModel):
    caller_username: str
    callee_username: str


class ReceiveCall(BaseModel):
    channelName: str



#endpoints

@router.post("/makeCall")
def joinCall(data: MakeCall, db: Session = Depends(deps.get_db)):
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



@router.post("/receiveCall")
def receiveCall(data: ReceiveCall):
    #returns an agora token and the channel name for the receiver to join a particular call room

    agora = Agora()

    channelName = data.channelName

    token = agora.generate_token(channelName)

    return {
        "token": token,
        "channelName": channelName
    }



#web sockets

@router.websocket("/callNotification")
async def call_socket_endpoint(websocket: WebSocket):
    """ Websocket for awaiting incoming call notifications
				
		Sends and Receives:
				A JSON response containing JSON object
                {
                    "caller_username": caller_username,
                    "callee_username": callee_username,
                    "channelName": channelName
                } 

	    Raises:
                WebSocketException [1013]: Unable to connect to web socket. Try again later.
                WebSocketException [1006]: Crosscheck to make sure you are sending the right data format: JSON object.
    """
    try:
        await notify.connect(websocket)
    
    except:
        return HTTPException(
            status_code=status.WS_1013_TRY_AGAIN_LATER,
            detail="Unable to connect to web socket. Try again later."
        )
    
    while True:
        try:
            await notify.broadcast(await websocket.receive_json())
        
        except:
            websocket.close()
            return HTTPException(
                status_code=status.WS_1006_ABNORMAL_CLOSURE,
                detail="Crosscheck to make sure you are sending the right data format: JSON object."
            )


@router.websocket("/callStatus")
async def call_socket_endpoint(websocket: WebSocket):
    """ Websocket for awaiting accepted or rejected call status messages
				
		Sends and Receives:
				A JSON response containing JSON object
                {
                    "caller_username": caller_username,
                    "callee_username": callee_username,
                    "channelName": channelName,
                    "call_status": accepted/rejected
                } 

	    Raises:
                WebSocketException [1013]: Unable to connect to web socket. Try again later.
                WebSocketException [1006]: Crosscheck to make sure you are sending the right data format: JSON object.
    """
    await notify.connect(websocket)
    while True:        
        await notify.broadcast(await websocket.receive_json())
