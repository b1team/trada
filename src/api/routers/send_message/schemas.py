from pydantic import BaseModel, validator
from typing import Optional


class MessagesSendSchema(BaseModel):
    content : str
    room_id: Optional[str] = None

    @validator("content")
    def content_validator(cls, value):
        if not value.strip():
            raise ValueError("content must not be empty")
        return value


    @validator("room_id")
    def receiver_id_validator(cls, value):
        if not value.strip():
            raise ValueError("room_id must not be empty")
        return value


class MessagesSendResponseSchema(BaseModel):
    message_id: Optional[str] = None
    content: Optional[str] = None
    sender_id: Optional[str] = None
    room_id: Optional[str] = None
    created_at: str
    seen: bool
    active: bool