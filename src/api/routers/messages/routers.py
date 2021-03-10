from fastapi import APIRouter
from src.services.crud.messages import message
from . import schemas
from fastapi.exceptions import HTTPException

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/messages", response_model=schemas.MessagesSaveResponeSchema)
def save_messages(message_new: schemas.MessagesSaveSchema):
    _message = message.save_message(
        message_new.content,
        message_new.senderId,
        message_new.sendername,
        message_new.recivedname)

    return _message.to_dict()


@router.put("/messages", tags=["messages"])
def update_message(message: schemas.MessagesUpdateSchema):
    update_message = message.update(message.mess_id,
                                    message.content)

    if update_message:
        return {"success": True}

    return {"success": False}


@router.delete("/messages/{message_id}", response_model=None)
def delete_message(message_id):
    if message_id is None:
        raise HTTPException(status_code=404, detail="Please enter a message id")
    delete_mess = message.delete(message_id)

    if delete_mess:
        return {"Message has been deleted"}

    return {"success": False}


@router.get("/messages", response_model=schemas.MessagesGetResponeSchema)
def get_messages(mess: schemas.MessagesGetSchema):
    _messages = message.messages_get(
        mess.sendername,
        mess.recivedname)
    # bi loi (TypeError: Window.fetch: HEAD or GET Request cannot have a body)
    if _messages is not None:
        return {"messages": _messages}

    return {"success": False}