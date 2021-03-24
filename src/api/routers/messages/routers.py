from datetime import datetime
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.services.crud import messages as message
from typing import Optional
from . import schemas

router = APIRouter(tags=["messages"])


@router.post("/messages", response_model=schemas.MessagesSaveResponeSchema)
def save_messages(message_new: schemas.MessagesSaveSchema):
    _message = message.save_message(message_new.content, message_new.sender_id,
                                    message_new.receiver_id)

    return _message.to_dict()


@router.put("/messages", response_model=schemas.BasicResponse)
def update_message(message_update: schemas.MessagesUpdateSchema):
    update_message = message.update(message_update.message_id,
                                    message_update.content)

    if update_message:
        return {"success": True}

    return {"success": False}


@router.delete("/messages/{message_id}", response_model=schemas.BasicResponse)
def delete_message(message_id: str):
    if message_id.strip() == "":
        raise HTTPException(status_code=404,
                            detail="message_id must not be space")
    delete_mess = message.delete(message_id)

    if delete_mess:
        return {"success": True}

    return {"success": False}


@router.get("/messages", response_model=None)
def get_messages(sender_id: Optional[str] = None,
                 receiver_id: Optional[str] = None,
                 start_time: Optional[datetime] = None,
                 end_time: Optional[datetime] = None):
    _messages = message.messages_get(sender_id, receiver_id, start_time,
                                     end_time)
    return {"messages": _messages, "count": len(_messages)}
