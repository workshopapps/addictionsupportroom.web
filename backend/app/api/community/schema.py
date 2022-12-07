from typing import Any
from pydantic import BaseModel



class ResponseModel(BaseModel):
    """Creates a response model for Emergencies.

    Provides a structure for providing a response to the Emergencies request.

    Provides a static method for success responses
    
    Attributes:
        status: The status of the response.
        message: The message of the response.
        data: The data of the response.
    """

    status: str
    message: str
    data: Any