from pydantic import BaseModel
from typing import Optional


class MessagesSaveSchema(BaseModel):
    content : str
    senderId: str
    sendername: Optional[str] = None
    recivedname:Optional[str] = None


class MessagesSaveResponeSchema(BaseModel):
    message_id: str
    content: str
    senderId: str
    sendername: Optional[str] = None
    recivedname: Optional[str] = None
    date: Optional[str] = None
    timestamp: Optional[str] = None
    seen: bool


class MessagesUpdateSchema(BaseModel):
    message_id: str
    content : str


class MessagesDeleteSchema(BaseModel):
    message_id: str