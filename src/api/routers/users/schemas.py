from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime


class CreateUserSchema(BaseModel):
    username: str
    password: str
    name: str

    @validator('username')
    def enter_username(cls, v):
        if v.strip() == "":
            raise ValueError('username cannot be a space ')
        return v

    @validator('password')
    def enter_password(cls, v):
        if v.strip() == "":
            raise ValueError('password cannot be a space ')
        return v


class CreateUserResponseSchema(BaseModel):
    user_id: str
    username: str
    name: Optional[str] = None
    avatar: Optional[str] = None
    created_at: datetime
    active: bool



class UserProfileResponseSchema(BaseModel):
    user_id: str
    username: str
    avatar: Optional[str] = None
    name: str
    created_at:datetime
    active: bool


class BasicResponse(BaseModel):
    success: bool = True

class UpdateUserSchema(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None


class UpdateUserResponseSchema(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None

