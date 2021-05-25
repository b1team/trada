from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from src.api.depends.auth import get_current_user
from src.config import settings
from src.libs.models.users import User
from src.services.crud import messages as message
from src.services.crud.messages import logic as message_logic
from src.services.crud.room import logic as room_logic
from src.services.crud.room.logic import room_members
from src.services.message_management.publish import publish_event

from . import schemas

router = APIRouter(tags=["messages"])


@router.post("/messages", response_model=schemas.MessagesSaveResponeSchema)
def save_messages(message_new: schemas.MessagesSaveSchema,
                  auth_user: User = Depends(get_current_user)):
    _message = message.save_message(message_new.content, str(auth_user.id),
                                    message_new.room_id)

    return _message.to_dict()


@router.put("/messages", response_model=schemas.BasicResponse)
def update_message(message_update: schemas.MessagesUpdateSchema,
                   auth_user: User = Depends(get_current_user)):
    if str(auth_user.id) != message_logic.get_user_id_by_message(
            message_update.message_id):
        raise HTTPException(status_code=403, detail='Permission denied')
    update_message = message.update(message_update.message_id,
                                    str(auth_user.id),
                                    message_update.content)

    members = room_members(message_update.room_id)
    for member in members:
        if str(member) != str(auth_user.id):
            event = {"event_type": "update",
                     "payload": {"room_id": message_update.room_id,
                                 "content": message_update.content,
                                 "message_id": message_update.message_id}}
            channel = f"{member}_notify"
            publish_event(redis_uri=settings.REDIS_URI,
                          channel=channel,
                          event=event)

    if update_message:
        return {"success": True}

    return {"success": False}


@router.delete("/messages", response_model=schemas.BasicResponse)
def delete_message(data: schemas.DeleteMessageSchema,
                   auth_user: User = Depends(get_current_user)):
    if data.message_id.strip() == "":
        raise HTTPException(status_code=404,
                            detail="message_id must not be space")
    if str(auth_user.id) != message_logic.get_user_id_by_message(data.message_id):
        raise HTTPException(status_code=403, detail='Permission denied')
    delete_mess = message.delete(data.message_id, str(auth_user.id))

    members = room_members(data.room_id)
    for member in members:
        if str(member) != str(auth_user.id):
            event = {"event_type": "delete_mess",
                     "payload": {"room_id": data.room_id,
                                 "message_id": data.message_id,
                                 "index": data.index}}
            channel = f"{member}_notify"
            publish_event(redis_uri=settings.REDIS_URI,
                          channel=channel,
                          event=event)

    if delete_mess:
        return {"success": True}

    return {"success": False}


@router.get("/messages/room", response_model=None)
def get_messages_in_room(room_id: Optional[str] = None,
                         start_time: Optional[datetime] = None,
                         end_time: Optional[datetime] = None,
                         auth_user: User = Depends(get_current_user)):
    if not room_logic.check_room_exists(room_id):
        raise HTTPException(status_code=404, detail="Room not found")
    if not room_logic.check_member_exists(room_id, str(auth_user.id)):
        raise HTTPException(status_code=404, detail="you not in this room")
    if start_time:
        # kiem tra thoi gian join group. lay cac message tu luc join thoi
        pass
    _messages = message.messages_get(room_id=room_id, start_time=start_time,
                                     end_time=end_time)
    return {"messages": _messages, "count": len(_messages)}


@router.get("/messages", response_model=None)
def get_all_messages(room_id: Optional[str] = None,
                     start_time: Optional[datetime] = None,
                     end_time: Optional[datetime] = None,
                     auth_user: User = Depends(get_current_user)):

    _messages = message.messages_get(str(auth_user.id), room_id, start_time,
                                     end_time)
    return {"messages": _messages, "count": len(_messages)}
