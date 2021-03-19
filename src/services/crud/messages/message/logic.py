from src.libs.models.message import Messages
from bson import ObjectId
from typing import Optional


def save_messages(
    content: str,
    senderId: str,
    sendername: Optional[str] = None,
    recivedname: Optional[str] = None,
    date: Optional[str] = None,
    timestamp: Optional[str] = None
):
    new_message = Messages(
        content=content,
        senderId=senderId,
        sendername=sendername,
        recivedname=recivedname,
        date=date,
        timestamp=timestamp)

    return new_message.save()


def get_messages(sendername, recivedname):
    messages = Messages.objects(sendername=sendername, recivedname=recivedname)
    list_messages = []
    for message in messages:
        list_messages.append(message)

    return list_messages


def get_one_message(message_id):
    return Messages.objects(id=ObjectId(message_id)).first()


def update_messages(
    message_id: str,
    content: str
):
    message = Messages.objects(id=ObjectId(message_id))
    filed = {
        "content": content,
    }

    message.update(**filed)

    return True


def delete_messages(sendername, recivedname, content):
    messages = Messages.objects(sendername=sendername,
                                recivedname=recivedname,
                                content=content)
    messages.delete()

    return True