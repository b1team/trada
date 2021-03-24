from pydantic import BaseModel, validator
from typing import Optional
from dateutil.parser import parser

class MessagesSaveSchema(BaseModel):
    content: str
    sender_id: str
    receiver_id: Optional[str] = None

    @validator("content")
    def content_validator(cls, value):
        if not value.strip():
            raise ValueError("content must not be empty")
        return value

    @validator("sender_id")
    def sender_id_validator(cls, value):
        if not value.strip():
            raise ValueError("sender_id must not be empty")
        return value

    @validator("receiver_id")
    def receiver_id_validator(cls, value):
        if not value.strip():
            raise ValueError("receiver_id must not be empty")
        return value


class MessagesSaveResponeSchema(BaseModel):
    message_id: str
    content: str
    sender_id: str
    receiver_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    seen: bool
    active: bool


class MessagesUpdateSchema(BaseModel):
    message_id: str
    content: str

    @validator("content")
    def content_validator(cls, value):
        if not value.strip():
            raise ValueError("content must not be empty")
        return value

    @validator("message_id")
    def message_id_validator(cls, value):
        if not value.strip():
            raise ValueError("message_id must not be empty")
        return value


class BasicResponse(BaseModel):
    success: bool