from pydantic import BaseModel
from typing import Optional


class MessagesSaveSchema(BaseModel):
    content : str
    senderId: Optional[str] = None
    sendername: Optional[str] = None
    recivedname: Optional[str] = None