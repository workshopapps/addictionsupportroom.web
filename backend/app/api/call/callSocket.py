from fastapi import APIRouter, WebSocket
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

@router.websocket("/")
async def call_waiting(websocket:WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            print(data)
        except:
            pass
            break
