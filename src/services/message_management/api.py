from typing import Optional

from src.api.exceptions import internal_errors, room_errors, user_errors
from src.config import settings
from src.services.crud.users.logic import check_user_exist
from src.services.crud.room.logic import check_room_exists, room_members

from . import logic
from .publish import publish_event


def send_message(content: str,
                 sender_id: Optional[str] = None,
                 room_id: Optional[str] = None):
    try:
        is_room = check_room_exists(room_id)
    except:
        raise internal_errors.InternalError(detail="Incorrect room id format")

    if not is_room:
        raise room_errors.NotFoundError(obj=f"Room {room_id}")

    try:
        sender_exist = check_user_exist(sender_id)
    except:
        raise internal_errors.InternalError(detail="Incorrect user id format")
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"Sender {sender_id}")

    if is_room:
        try:
            message = logic.send_to_user(content, sender_id, room_id)
        except:
            raise internal_errors.InternalError(detail="Check id format")

        event = {"event_type": "new_message", "message": message.to_dict()}

        members = room_members(room_id)
        for member in members:
            publish_event(redis_uri=settings.REDIS_URI,
                          channel=member,
                          event=event)
        return message

    return False
