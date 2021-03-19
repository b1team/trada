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


class MessagesGetSchema(BaseModel):
    sendername: Optional[str] = None
    recivedname: Optional[str] = None


class MessagesGetResponeSchema(BaseModel):
    message_id: str
    content: str
    senderId: str
    sendername: str
    recivedname: str
    date: str
    timestamp: str