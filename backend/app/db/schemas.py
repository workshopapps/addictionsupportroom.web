from typing import Any, Dict

from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: str
    message: str
    data: Any

    @staticmethod
    def success(data: Any, message: str = "success") -> Dict[str, Any]:
        return ResponseModel(status="success", message=message, data=data).dict()

    @staticmethod
    def error(message: str) -> Dict[str, Any]:
        ResponseModel(status="error", data={"detail": message}).dict()