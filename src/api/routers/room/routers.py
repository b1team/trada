from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from src.api.depends.auth import get_current_user
from src.libs.models.users import User
from src.services.crud import room
from src.services.crud.room import logic

from . import schemas

router = APIRouter(tags=["room"])


@router.post("/rooms")
def create_room(room_name: str, auth_user: User = Depends(get_current_user)):
    if room_name.strip() == "":
        raise HTTPException(status_code=411, detail="Enter your room name")
    _room = room.create_room(room_name, str(auth_user.id))

    return _room


@router.delete("/rooms")
def delete_room(room_id: str, auth_user: User = Depends(get_current_user)):
    if not logic.check_is_admin(room_id, str(auth_user.id)):
        raise HTTPException(status_code=403, detail="Permission denied.")
    _delete_room = room.delete_room(room_id)

    if _delete_room:
        return {"success": True}
    return {"success": False}


@router.post("/rooms/invite")
def invite_member(data: schemas.BasicSchemas):
    member = room.invite_member(room_id=data.room_id,
                                member_name=data.member_name)

    return member.to_dict()


@router.delete("/rooms/remove")
def delete_member(data: schemas.BasicSchemas,
                  auth_user: User = Depends(get_current_user)):
    if not logic.check_is_admin(data.room_id, str(auth_user.id)):
        raise HTTPException(status_code=403, detail="Permission denied.")
    member = room.delete_member(room_id=data.room_id,
                                member_name=data.member_name)

    if member:
        return {"success": True}
    return {"success": False}


@router.get("/rooms")
def load_rooms(auth_user: User = Depends(get_current_user)):
    rooms = room.get_rooms(str(auth_user.id))

    return {"rooms": rooms, "count": len(rooms)}


@router.put("/rooms/update")
def update_room(data: schemas.UpdateRoomSchemas,
                auth_user: User = Depends(get_current_user)):
    if (data.room_name.strip() or data.avatar.strip()) == "":
        return
    new_Room_info = room.room_update(room_id=data.room_id,
                                     room_name=data.room_name,
                                     avatar=data.avatar)
    _room = {
        "room_id": data.room_id,
        "room_name": data.room_name,
        "avatar": data.avatar
    }
    return {"room": _room}


@router.delete("/rooms/getout")
def getout_room(data: schemas.BasicSchemas,
                auth_user: User = Depends(get_current_user)):
    if not logic.check_is_member(data.room_id, str(auth_user.id)):
        raise HTTPException(status_code=403, detail="Permission denied.")
    member = room.delete_member(room_id=data.room_id,
                                member_name=data.member_name)

    if member:
        return {"success": True}
    return {"success": False}


@router.get("/rooms/members")
def get_members(room_id: str,
                auth_user: User = Depends(get_current_user)):
    members = room.members(room_id)

    return {"members": members}