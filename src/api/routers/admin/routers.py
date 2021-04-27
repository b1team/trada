from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from src.api.depends.auth import get_current_user
from src.config import settings
from src.libs.models.users import User
from src.services import admin
from src.services.auth import AuthService

from . import schemas

router = APIRouter(tags=["admin"])


@router.post("/admin/user", response_model=schemas.CreateUserResponseSchema)
def create_user(user: schemas.CreateUserSchema):
    auth = AuthService(settings.TOKEN_SECRET_KEY)
    hashed_password = auth.hash_password(user.password)
    new_user = admin.create_user(username=user.username,
                                 password=hashed_password,
                                 name=user.name)

    return new_user.to_dict()


@router.get("/admin/user")
def load_users():
    users = admin.load_users()

    return {"users": users, "count": len(users)}


@router.put("/admin/user")
def disable_user(user_id: str):
    user = admin.disable_user(user_id)

    if user:
        return {"success": True}
    return {"success": False}


@router.post("/admin/rooms")
def create_room(room_name: str, auth_user: User = Depends(get_current_user)):
    if room_name.strip() == "":
        raise HTTPException(status_code=411, detail="Enter your room name")
    _room = admin.create_room(room_name, str(auth_user.id))

    return _room


@router.get("/admin/rooms")
def load_rooms():
    rooms = admin.load_rooms()

    return {"rooms": rooms, "count": len(rooms)}


@router.delete("/adin/rooms")
def delete_room(room_id: str):
    _delete_room = admin.remove_room(room_id)

    if _delete_room:
        return {"success": True}
    return {"success": False}


@router.get("/admin/messages")
def get_messages(
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
):

    _messages = admin.messages_count(start_time=start_time, end_time=end_time)

    return {"messages": _messages}
