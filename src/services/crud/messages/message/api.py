from typing import Optional

from src.api.exceptions import user_errors
from src.services.crud.groups.group.logic import check_group_exists
from src.services.crud.users.logic import check_user_exist

from . import logic


def save_message(
    content: str,
    sender_id: str,
    receiver_id: Optional[str] = None,
):
    sender_exist = check_user_exist(sender_id) or check_group_exists(sender_id)
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"User {sender_id}")
    receiver_exist = check_user_exist(receiver_id) or check_group_exists(receiver_id)
    if not receiver_exist:
        raise user_errors.NotFoundError(obj=f"Receiver {receiver_id}")


    return logic.save_messages(content, sender_id, receiver_id)


def get(sendername:str, recivedname:str):
    message = get_messages(sendername, recivedname)

    if message is not None:
        return message

    return False


def delete(sendername:str, recivedname:str, content:str):
    del_message = delete_messages(sendername, recivedname, content)

    if del_message is not None:
        return True

    return False


def update(message_id:str, content:str):
    update_message = update_messages(message_id, content)

    if update_message is not None:
        return True

    return False
