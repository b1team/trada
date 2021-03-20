from typing import Optional

from src.api.exceptions import user_errors, internal_errors
from src.services.crud.users.logic import check_user_exist

from . import logic


def save_message(
    content: str,
    sender_id: str,
    receiver_id: Optional[str] = None,
):
    try:
        sender_exist = check_user_exist(sender_id)
    except:
        raise internal_errors.InternalError(detail="Incorrect id format")
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"User {sender_id}")

    try:
        receiver_exist = check_user_exist(receiver_id)
    except:
        raise internal_errors.InternalError(detail="Incorrect id format")
    if not receiver_exist:
        raise user_errors.NotFoundError(obj=f"Receiver {receiver_id}")

    return logic.save_messages(content, sender_id, receiver_id)


def messages_get(sender_id: str, receiver_id: str):
    try:
        sender_exist = check_user_exist(sender_id)
    except:
        raise internal_errors.InternalError(detail="Incorrect id format")
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"User {sender_id}")

    try:
        recived_exist = check_user_exist(receiver_id)
    except:
        raise internal_errors.InternalError(detail="Incorrect id format")
    if not recived_exist:
        raise user_errors.NotFoundError(obj=f"User {receiver_id}")

    return logic.get_all_messages(sender_id, receiver_id)


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

