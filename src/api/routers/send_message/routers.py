from fastapi import APIRouter
from src.services.crud.messages import send
from . import schemas

router = APIRouter(prefix="/send_message", tags=["send_message"])

@router.post("/send", response_model=None)
def send_messages(message: schemas.MessagesSaveSchema):
    messages = send.send_message(
        message.content,
        message.senderId,
        message.sendername,
        message.recivedname)

    if messages is not None:
        return {"success": messages}

    return {"success": False}