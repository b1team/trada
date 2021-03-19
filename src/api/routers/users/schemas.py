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



class BasicResponse(BaseModel):
    success: bool = True

class UpdateUserSchema(BaseModel):
    name: Optional[str] = None
    avatar: Optional[str] = None


class UpdateUserResponseSchema(BaseModel):
    name: Optional[str] = None
    avatar: Optional[str] = None