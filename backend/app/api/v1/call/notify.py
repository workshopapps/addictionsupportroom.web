from fastapi import WebSocket
from typing import List
import json


class NotificationManager:
    def __init__(self):
        self.connections: List[WebSocket] = []
    
    async def connect(self, websocket:WebSocket):
        await websocket.accept()
        self.connections.append(websocket)
    
    async def broadcast(self, data: json):
        for connection in self.connections:
            await connection.send_json(data)

