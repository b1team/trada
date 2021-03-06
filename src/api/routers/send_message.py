from fastapi import APIRouter
from src.services.crud.messages import send
from ..basemodels import Messages_save

router = APIRouter(prefix="/send_message", tags=["send_message"])

@router.post("/send", tags=["send_message"])
def send_messages(message: Messages_save):
    messages = send.send_message(message.content,
                                 message.senderId,
                                 message.sendername,
                                 message.recivedname)

    if messages is not None:
        return messages

    return {"success": False}