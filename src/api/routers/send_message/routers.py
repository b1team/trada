from fastapi import APIRouter
from fastapi.param_functions import Depends
from src.api.depends.auth import get_current_user
from src.libs.models.users import User
from src.services import message_management as send
from src.services.crud.room import logic as room_logic
from . import schemas
from fastapi.exceptions import HTTPException

router = APIRouter(prefix="/message_management", tags=["send_message"])


@router.post("/send_message",
             response_model=schemas.MessagesSendResponseSchema)
def send_messages(message: schemas.MessagesSendSchema,
                  auth_user: User = Depends(get_current_user)):
    if not room_logic.check_member_exists(message.room_id, str(auth_user.id)):
        raise HTTPException(status_code=404, detail="you not in this room")

    messages = send.send_message(message.content, str(auth_user.id),
                                 message.room_id)

    if messages:
        return messages.to_dict()

    return {"success": False}
