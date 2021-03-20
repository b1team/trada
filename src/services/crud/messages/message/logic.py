from typing import Optional

from bson import ObjectId
from src.libs.models.message import Messages


def save_messages(
    content: str,
    sender_id: str,
    receiver_id: Optional[str] = None,
):
    new_message = Messages(content=content,
                           sender_id=sender_id,
                           receiver_id=receiver_id)

    return new_message.save()


def get_all_messages(
    sender_id: str,
    receiver_id: str,
):
    messages = Messages.objects(sendername=sender_id, recivedname=receiver_id)

    list_messages = []
    for message in messages:
        list_messages.append(message.to_dict())

    return list_messages


def get_one_message(message_id: str):
    return Messages.objects(id=ObjectId(message_id)).first()


def update_messages(message_id: str, content: str):
    message = Messages.objects(id=ObjectId(message_id))
    filed = {
        "content": content,
    }

    message.update(**filed)

    return True


def delete_messages(message_id: str):
    messages = Messages.objects(id=ObjectId(message_id))
    messages.delete()

    return True
