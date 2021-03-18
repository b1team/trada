from typing import Optional

from bson import ObjectId
from src.libs.models.message import Messages


def save_messages(
    content: str,
    sender_id: str,
    receiver_id: Optional[str] = None,
):
    new_message = Messages(
        content=content,
        sender_id=sender_id,
        receiver_id=receiver_id)

    return new_message.save()


def get_messages(sendername, recivedname):
    messages = Messages.objects(sendername=sendername, recivedname=recivedname)
    list_messages = []
    for message in messages:
        list_messages.append(message)

    return list_messages


def update_messages(message_id, content):
    message = Messages.objects(message_id=ObjectId(message_id))
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
