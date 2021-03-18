from pydantic import BaseModel
from typing import Optional


class MessagesSaveSchema(BaseModel):
    content : str
    sender_id: str
    reciver_id:Optional[str] = None


class MessagesSaveResponeSchema(BaseModel):
    message_id: str
    content: str
    sender_id: str
    reciver_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    seen: bool


class MessagesUpdateSchema(BaseModel):
    message_id: str
    content : str


class MessagesDeleteSchema(BaseModel):
    message_id: str