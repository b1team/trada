from typing import Optional

from src.api.exceptions import internal_errors, user_errors
from src.config import settings
from src.services.crud.users.logic import check_user_exist

from .logic import send_private
from .publish import publish_event


def send_message(content: str,
                 sender_id: Optional[str] = None,
                 receiver_id: Optional[str] = None):
    try:
        is_user = check_user_exist(receiver_id)
    except:
        raise internal_errors.InternalError(detail="Incorrect id format")

    if not is_user:
        raise user_errors.NotFoundError(obj=f"Reciver {receiver_id}")

    try:
        sender_exist = check_user_exist(sender_id)
    except:
        raise internal_errors.InternalError(detail="Incorrect id format")
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"Sender {sender_id}")

    if is_user:
        try:
            message = send_private(content, sender_id, receiver_id)
        except:
            raise internal_errors.InternalError(detail="Check id format")

        event = {"event_type": "new_message", "message": message.to_dict()}

        publish_event(redis_uri=settings.REDIS_URI,
                      channel=receiver_id,
                      event=event)
        return message

    return False
