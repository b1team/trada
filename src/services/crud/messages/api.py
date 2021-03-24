from typing import Optional

from src.api.exceptions import user_errors, internal_errors, room_errors
from src.services.crud.users.logic import check_user_exist
from src.services.crud.room.logic import check_room_exists, check_room_exists

from . import logic


def save_message(content: str,
                 sender_id: Optional[str] = None,
                 room_id: Optional[str] = None):
    try:
        sender_exist = check_user_exist(sender_id)
    except:
        raise user_errors.IdFormatError()

    try:
        room_exist = check_room_exists(room_id)
    except:
        raise room_errors.IdFormatError()

    return logic.save_messages(content, sender_id, room_id)


def messages_get(sender_id: Optional[str] = None,
                 room_id: Optional[str] = None,
                 start_time: Optional[str] = None,
                 end_time: Optional[str] = None):
    try:
        sender_exist = check_user_exist(sender_id)
    except:
        raise user_errors.IdFormatError()

    try:
        receiver_exist = check_room_exists(room_id)
    except:
        raise user_errors.IdFormatError()

    return logic.get_all_messages(sender_id, room_id, start_time, end_time)


def delete(message_id: str):
    try:
        del_message = logic.delete_messages(message_id)
    except:
        raise internal_errors.InternalError(detail="incorrect id format")

    if not del_message:
        raise user_errors.NotFoundError(obj=f"Message {message_id}")
    return del_message


def update(message_id: str, content: str):
    try:
        message_exist = logic.get_one_message(message_id)
    except:
        raise internal_errors.InternalError(detail="incorrect id format")

    if message_exist:
        try:
            return logic.update_messages(message_id, content)
        except:
            raise internal_errors.InternalError(detail="Update failed")
    else:
        return user_errors.NotFoundError(obj=f"Messages {message_id}")
