from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CreateUserSchema(BaseModel):
    username: str
    password: str
    name: Optional[str] = None
    avatar: Optional[str] = None


class CreateUserResponseSchema(BaseModel):
    user_id: str
    username: str
    name: Optional[str] = None
    avatar: Optional[str] = None
    created_at: datetime


class UserProfileResponseSchema(BaseModel):
    user_id: str
    username: str
    avatar: Optional[str] = None
    password: Optional[str] = None
    name: str
    created_at:datetime