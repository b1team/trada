from src.services.crud.groups import group
from pydantic import BaseModel

class Messages_save(BaseModel):
    content : str
    senderId: str
    sendername: str
    recivedname:str


class Messages_ud(BaseModel):
    mess_id: str
    content : str


class User(BaseModel):
    username: str
    password: str


class User_update(BaseModel):
    username: str
    password: str
    avatar_url: str
    name: str


class join_info(BaseModel):
    username: str
    group_name: str