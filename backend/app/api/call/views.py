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
from fastapi.requests import Request


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



@router.post("/receiveCall",
    status_code=status.HTTP_201_CREATED,
    responses=
    {
        424:{
            "description": "Something went wrong. Try again later."
            },
        405:{
            "description": "Method not allowed"
            }
    }
    )
def receiveCall(request: Request, data: ReceiveCall):
    """ Returns an agora token and the channel name for the receiver to join a particular call room
        
        Args:
				channelName: channel name to join
				
		Returns:
				A JSON response containing the status code and message
                {
                    "status_code": 201,
                    "detail": "Agora token created",
                    "data": data = {
                        "token": token,
                        "channelName": channelName
                        }
                    } 
	    Raises:
                HTTPException [405]: Method not allowed
                HTTPException [424]: Something went wrong. Try again later.
    """

    if request.method == "POST":

        try:
            agora = Agora()

            channelName = data.channelName

            token = agora.generate_token(channelName)
        
        except:
            return HTTPException(
                status_code=status.HTTP_424_FAILED_DEPENDENCY,
                detail="Something went wrong. Try again later."
            )
        
        data = {
            "token": token,
            "channelName": channelName
        }

        return {
            "status_code": status.HTTP_201_CREATED,
            "detail": "Agora token created",
            "data": data
        }
    
    else:
        return HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Method not allowed"
        )



#web sockets

@router.websocket("/callNotification")
async def call_socket_endpoint(websocket: WebSocket):
    #websocket for waiting for incoming call notifications
    await notify.connect(websocket)
    while True:        
        data = await websocket.receive_json()
        await notify.broadcast(data)


@router.websocket("/callStatus")
async def call_socket_endpoint(websocket: WebSocket):
    #websocket for waiting for accepted or rejected call status messages
    await notify.connect(websocket)
    while True:        
        data = await websocket.receive_json()
        await notify.broadcast(data)
