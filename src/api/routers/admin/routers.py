from datetime import datetime
from typing import List, Optional, Dict, Any

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from src.api.admin_depends.auth import get_current_user
from src.config import settings
from src.libs.models.admin import Admin as AdminModel
from src.services import admin
from src.services.auth import AdminAuthService

from . import schemas

router = APIRouter(tags=["admin"])


@router.post("/admin/user", response_model=schemas.CreateUserResponseSchema)
def create_user(user: schemas.CreateUserSchema):
    auth = AdminAuthService(settings.ADMIN_TOKEN_SECRET_KEY)
    hashed_password = auth.hash_password(user.password)
    new_user = admin.create_user(username=user.username,
                                 password=hashed_password,
                                 name=user.name)

    return new_user.to_dict()


@router.post("/admin/ad", response_model=schemas.CreateUserResponseSchema)
def create_admin(user: schemas.CreateUserSchema):
    auth = AdminAuthService(settings.ADMIN_TOKEN_SECRET_KEY)
    hashed_password = auth.hash_password(user.password)
    new_user = admin.create_admin(username=user.username,
                                  password=hashed_password,
                                  name=user.name)

    return new_user.to_dict()


@router.get("/admin/me", response_model=schemas.UserProfileResponseSchema)
def get_me(user: AdminModel = Depends(get_current_user)):
    return user.to_dict()


@router.get("/admin/{username}",
            response_model=schemas.UserProfileResponseSchema)
def get_admin_profile(username: str):
    if username.strip() == "":
        raise HTTPException(status_code=411,
                            detail="Username must not be space")
    _user = admin.get_admin(username)

    return _user.to_dict()


@router.put("/admin/ad", response_model=schemas.UpdateUserResponseSchema)
def update_admin(user: schemas.UpdateUserSchema,
                 auth_user: AdminModel = Depends(get_current_user)):
    new_user_info = admin.update_admin(str(auth_user.id), user.username,
                                       user.avatar, user.name)
    if new_user_info:
        return user


@router.get("/admin/user/all")
def users_load():
    try:
        print("VAO DAY")
        users = admin.load_users()
    except Exception as e:
        print("LOAD USER ERROR")
        raise e

    return {"users": users, "count": len(users)}


@router.put("/admin/user")
def disable_user(user_id: str):
    user = admin.disable_user(user_id)

    if user:
        return {"success": True}
    return {"success": False}


@router.post("/admin/rooms")
def create_room(room_name: str, auth_user: AdminModel = Depends(get_current_user)):
    if room_name.strip() == "":
        raise HTTPException(status_code=411, detail="Enter your room name")
    _room = admin.create_room(room_name, str(auth_user.id))

    return _room


@router.get("/admin/rooms/all")
def load_rooms():
    rooms = admin.load_rooms()

    return {"rooms": rooms, "count": len(rooms)}


@router.delete("/admin/rooms")
def delete_room(room_id: str):
    _delete_room = admin.remove_room(room_id)

    if _delete_room:
        return {"success": True}
    return {"success": False}


@router.get("/admin/messages/all")
def get_messages(
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
):

    _messages = admin.messages_count(start_time=start_time, end_time=end_time)

    return {"messages": _messages}
