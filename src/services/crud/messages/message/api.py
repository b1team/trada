from . import logic
import datetime
from typing import Optional
from src.api.exceptions import user_errors
from src.services.crud.users.logic import get_user
from src.services.crud.groups.group.logic import get_group


def save_message(
    content: str,
    senderId: str,
    sendername: Optional[str] = None,
    recivedname: Optional[str] = None,
):
    sender_exist = get_user(sendername) or get_group(sendername)
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"User {sendername}")
    receiver_exist = get_group(recivedname) or get_group(recivedname)
    if not receiver_exist:
        raise user_errors.NotFoundError(obj=f"Receiver {recivedname}")

    date = datetime.datetime.utcnow().strftime("%d %B")
    timestamp = datetime.datetime.utcnow().strftime("%H:%M")

    return logic.save_messages(content, senderId, sendername, recivedname, date, timestamp)


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