from fastapi import APIRouter
from src.services import message_management as send

from . import schemas

router = APIRouter(prefix="/message_management", tags=["send_message"])


@router.post("/send_message",
             response_model=schemas.MessagesSendResponseSchema)
def send_messages(message: schemas.MessagesSendSchema):
    messages = send.send_message(message.content, message.sender_id,
                                 message.room_id)

    if messages:
        return messages.to_dict()

    return {"success": False}
