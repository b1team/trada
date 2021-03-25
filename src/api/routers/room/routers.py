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
    if not logic.check_owner(room_id, str(auth_user.id)):
        raise HTTPException(status_code=403, detail="Permission denied.")
    _delete_room = room.delete_room(room_id)

    if _delete_room:
        return {"success": True}
    return {"success": False}


@router.post("/rooms/invite")
def invite_member(data: schemas.BasicSchemas):
    member = room.invite_member(room_id=data.room_id, member_id=data.member_id)

    return member.to_dict()


@router.delete("/rooms/remove")
def delete_member(data: schemas.BasicSchemas,
                  auth_user: User = Depends(get_current_user)):
    if not logic.check_owner(data.room_id, str(auth_user.id)):
        raise HTTPException(status_code=403, detail="Permission denied.")
    member = room.delete_member(room_id=data.room_id, member_id=data.member_id)

    if member:
        return {"success": True}
    return {"success": False}


@router.get("/room")
def load_rooms(auth_user: User = Depends(get_current_user)):
    rooms = room.get_rooms(str(auth_user.id))

    return {"rooms": rooms, "count": len(rooms)}