from fastapi import APIRouter
from src.services.crud.messages import message
from ..basemodels import Messages_save, Messages_ud

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/messages", tags=["messages"])
def save_messages(message: Messages_save):
    message_save = message.save(message.content,
                                message.senderId,
                                message.sendername,
                                message.recivedname)

    if message_save:
        return {"success": True}

    return {"success": False}


@router.put("/messages", tags=["messages"])
def update_message(message: Messages_ud):
    update_message = message.update(message.mess_id,
                                    message.content)

    if update_message:
        return {"success": True}

    return {"success": False}


@router.delete("/messages", tags=["messages"])
def delete_message(message: Messages_ud):
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