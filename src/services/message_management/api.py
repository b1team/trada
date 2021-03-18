from datetime import datetime
from typing import Optional

from src.api.exceptions import user_errors
from src.config import settings
from src.services.crud.groups.group.logic import check_group_exists
from src.services.crud.users.logic import check_user_exist

from .logic import send_group, send_private
from .publish import publish_event


def send_message(content: str,
                 sender_id: Optional[str] = None,
                 receiver_id: Optional[str] = None):
    # check reciver
    is_group = check_group_exists(receiver_id)
    is_user = check_user_exist(receiver_id)

    if not (is_group or is_user):
        raise user_errors.NotFoundError(obj=f"Reciver {receiver_id}")

    sender_exist = check_user_exist(sender_id) or check_group_exists(sender_id)
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"Sender {sender_id}")

    if is_user:
        message = send_private(content, sender_id, receiver_id)
        event = {"event_type": "new_message", "message": message.to_dict()}
        publish_event(redis_uri=settings.REDIS_URI,
                      channel=receiver_id,
                      event=event)
        return message

    if is_group:
        send_to_group = send_group(content, sender_id)

        return {
            "success": f"send to group {receiver_id}",
            "from": sender_id,
            "content": content,
            "send_at": str(datetime.utcnow())
        }

    return False
