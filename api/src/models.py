
# Generic message model for endpoints responses
from pydantic import BaseModel

class Message(BaseModel):
    message: str