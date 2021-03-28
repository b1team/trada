from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from src.api.depends.auth import get_current_user
from src.libs.models.users import User
from src.services.crud import messages as message
from src.services.crud.messages import logic as message_logic
from src.services.crud.room import logic as room_logic

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

    if update_message:
        return {"success": True}

    return {"success": False}


@router.delete("/messages/{message_id}", response_model=schemas.BasicResponse)
def delete_message(message_id: str,
                   auth_user: User = Depends(get_current_user)):
    if message_id.strip() == "":
        raise HTTPException(status_code=404,
                            detail="message_id must not be space")
    if str(auth_user.id) != message_logic.get_user_id_by_message(message_id):
        raise HTTPException(status_code=403, detail='Permission denied')
    delete_mess = message.delete(message_id, str(auth_user.id))

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

    _messages = message.messages_get(str(auth_user.id), room_id, start_time,
                                     end_time)
    return {"messages": _messages, "count": len(_messages)}


@router.get("/messages", response_model=None)
def get_all_messages(room_id: Optional[str] = None,
                     start_time: Optional[datetime] = None,
                     end_time: Optional[datetime] = None,
                     auth_user: User = Depends(get_current_user)):

    _messages = message.messages_get(str(auth_user.id), room_id, start_time,
                                     end_time)
    return {"messages": _messages, "count": len(_messages)}
