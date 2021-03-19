from re import S
from pydantic import BaseModel
from typing import (
    Dict,
    Optional,
    List)
from datetime import date, datetime


class CreateGroupSchema(BaseModel):
    group_name: str
    user_created: str


class LastMessage(BaseModel):
    content: str
    senderId: str
    username: str
    avatar: Optional[str] = None
    timestamp: str
    seen: bool
    new: bool


class Members(BaseModel):
    member_name: str


class CreateGroupResponseSchema(BaseModel):
    group_id: str
    group_name: str 
    group_avatar: Optional[str] = None
    unreadCount: int = 0
    user_created: str
    created_at: datetime


class UpdateGroupSchema(BaseModel):
    group_name: str
    avatar: Optional[str] = None