from datetime import datetime
from typing import Optional
from bson import ObjectId
from src.libs.models.message import Messages
from src.services.crud.users.logic import get_public_user_info


def save_messages(content: str,
                  sender_id: str,
                  receiver_id: Optional[str] = None):
    new_message = Messages(content=content,
                           sender_id=sender_id,
                           receiver_id=receiver_id)

    return new_message.save()


def get_all_messages(sender_id: Optional[str] = None,
                     receiver_id: Optional[str] = None,
                     start_time: Optional[datetime] = None,
                     end_time: Optional[datetime] = None):
    filters = dict()

    if sender_id:
        filters.update({"sender_id": sender_id})
    if receiver_id:
        filters.update({"receiver_id": receiver_id})
    if start_time:
        filters.update({"created_at__gte": start_time})
    if end_time:
        filters.update({"created_at__lte": end_time})

    messages = Messages.objects(**filters)
    list_messages = []
    _users = {}

    for message in messages:
        if message.sender_id not in _users:
            _users[message.sender_id] = get_public_user_info(message.sender_id)

        if message.receiver_id not in _users:
            _users[message.receiver_id] = get_public_user_info(message.receiver_id)

        data = message.to_dict()
        data["sender"] = _users.get(message.sender_id)
        data["receiver"] = _users.get(message.receiver_id)
        data.pop("sender_id")
        data.pop("receiver_id")

        list_messages.append(data)

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
