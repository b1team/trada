from fastapi import APIRouter
from src.services.crud.messages import message
from . import schemas
from fastapi.exceptions import HTTPException

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/messages", response_model=schemas.MessagesSaveResponeSchema)
def save_messages(message_new: schemas.MessagesSaveSchema):
    _message = message.save_message(
        message_new.content,
        message_new.sender_id,
        message_new.reciver_id)

    return _message.to_dict()


@router.put("/messages", response_model=None)
def update_message(message_update: schemas.MessagesUpdateSchema):
    update_message = message.update(
        message_update.message_id,
        message_update.content)

    if update_message:
        return {"Message has been update"}
    return {"success": False}


@router.delete("/messages/{message_id}", response_model=None)
def delete_message(message_id):
    if message_id is None:
        raise HTTPException(status_code=404, detail="Please enter a message id")
    delete_mess = message.delete(message_id)

    if delete_mess:
        return {"Message has been deleted"}

    return {"success": False}


@router.get("/messages/{sendername}", response_model=None)
def get_messages(sendername: str, recivedname: str):
    if (recivedname is None) or (sendername is None):
        raise HTTPException(status_code=404, detail="Please enter a full info")
    _messages = message.messages_get(
        sendername,
        recivedname)
    if _messages is not None:
        return {"messages": _messages}

    return {"success": False}