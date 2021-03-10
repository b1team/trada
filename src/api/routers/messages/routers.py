from fastapi import APIRouter
from src.services.crud.messages import message
from . import schemas

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


@router.delete("/messages", tags=["messages"])
def delete_message(message: schemas.MessagesDeleteSchema):
    delete_mess = message.delete(message.sendername,
                                 message.recivedname,
                                 message.content)

    if delete_mess:
        return {"success": True}

    return {"success": False}


@router.get("/messages/{sendername}/{receivedname}", tags=["messages"])
def get_message(sendername, recivedname):
    messages = message.get(sendername, recivedname)

    if messages is not None:
        return {"messages": messages}

    return {"success": False}