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


def messages_get(
    sendername: str,
    recivedname: str
):
    sender_exist = get_user(sendername)
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"User {sendername}")
    recived_exist = get_user(recivedname) or get_group(recivedname)
    if not recived_exist:
        raise user_errors.NotFoundError(obj=f"User {recivedname}")

    return logic.get_all_messages(sendername, recivedname)



def delete(message_id: str):
    del_message = logic.delete_messages(message_id)

    if not del_message:
        raise user_errors.NotFoundError(obj=f"Message")
    return del_message


def update(
    message_id: str,
    content: str
):
    message_exist = logic.get_one_message(message_id)
    if not message_exist:
        return user_errors.NotFoundError(obj=f"Messages")
    return logic.update_messages(message_id, content)
