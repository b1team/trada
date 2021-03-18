from pydantic import BaseModel, validator
from typing import Optional


class MessagesSendSchema(BaseModel):
    content : str
    sender_id: str
    receiver_id: str

    @validator("content")
    def content_validator(cls, value):
        if not value.strip():
            raise ValueError("content must not be empty")
        return value


class MessagesSendResponseSchema(BaseModel):
    message_id: Optional[str] = None
    content: Optional[str] = None
    sender_id: Optional[str] = None
    receiver_id: Optional[str] = None
    created_at: str
    seen: bool