from .logic import (save_messages,
                    delete_messages,
                    update_messages,
                    get_messages)
import datetime
from bson import ObjectId


def save(content:str, senderId:ObjectId, sendername:str, recivedname:str):
    date = datetime.datetime.utcnow().strftime("%d %B")
    timestamp = datetime.datetime.utcnow().strftime("%H:%M")
    senderId = ObjectId(senderId)
    message = save_messages(content, senderId, sendername, recivedname, date, timestamp)
    if message:
        return True

    return False


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