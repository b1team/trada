from fastapi import APIRouter
from src.services.crud import room
from fastapi.exceptions import HTTPException

from . import schemas

router = APIRouter(tags=["room"])


@router.post("/rooms")
def create_room(room_name: str, user_id: str):
    if room_name.strip() == "":
        raise HTTPException(status_code=411, detail="Enter your room name")
    _room = room.create_room(room_name, user_id)

    return _room


@router.delete("/rooms")
def delete_room(room_id: str):
    _delete_room = room.delete_room(room_id)

    if _delete_room:
        return {"success": True}
    return {"success": False}


@router.post("/rooms/invite")
def invite_member(data: schemas.BasicSchemas):
    member = room.invite_member(room_id=data.room_id, member_id=data.member_id)

    return member.to_dict()


@router.delete("/rooms/remove")
def delete_member(data: schemas.BasicSchemas):
    member = room.delete_member(room_id=data.room_id, member_id=data.member_id)

    if member:
        return {"success": True}
    return {"success": False}
