from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.services.crud.messages import message

from . import schemas

router = APIRouter(prefix="/messages", tags=["messages"])


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
def delete_message(message_id):
    if message_id is None:
        raise HTTPException(status_code=404,
                            detail="Please enter a message id")
    delete_mess = message.delete(message_id)

    if delete_mess:
        return {"success": True}

    return {"success": False}


@router.get("/messages/{sender_id}",
            response_model=schemas.MessagesSaveResponeSchema)
def get_messages(sender_id: str, receiver_id: str):
    _messages = message.messages_get(
        sender_id,
        receiver_id,
    )
    if _messages is not None:
        return _messages

    return {"success": False}
