from datetime import datetime
from typing import Optional
from bson import ObjectId
from src.libs.models.message import Messages
from src.services.crud.users.logic import get_public_user_info
from src.services.crud.room import logic


def save_messages(content: str,
                  sender_id: Optional[str] = None,
                  room_id: Optional[str] = None):
    new_message = Messages(content=content,
                           sender_id=sender_id,
                           room_id=room_id)

    return new_message.save()


def get_all_messages(sender_id: Optional[str] = None,
                     room_id: Optional[str] = None,
                     start_time: Optional[datetime] = None,
                     end_time: Optional[datetime] = None):
    filters = dict()

    if sender_id:
        filters.update({"sender_id": sender_id})
    if room_id:
        filters.update({"room_id": room_id})
    if start_time:
        filters.update({"created_at__gte": start_time})
    if end_time:
        filters.update({"created_at__lte": end_time})
    filters.update({"active": True})

    messages = Messages.objects(**filters)
    list_messages = []
    _users = {}

    for message in messages:
        if message.sender_id not in _users:
            _users[message.sender_id] = get_public_user_info(message.sender_id)

        if message.room_id not in _users:
            _users[message.room_id] = logic.get_room_info(message.room_id)

        data = message.to_dict()
        data["sender"] = _users.get(message.sender_id)
        data["room"] = _users.get(message.room_id)
        data.pop("sender_id")
        data.pop("room_id")

        list_messages.append(data)

    return list_messages


def get_one_message(message_id: str):
    return Messages.objects(id=ObjectId(message_id)).first()


def update_messages(message_id: str, user_id: str, content: str):
    message = Messages.objects(id=ObjectId(message_id))
    if message.first().sender_id != user_id:
        return
    filed = {
        "content": content,
    }
    message.update(**filed)

    return True


def delete_messages(message_id: str, user_id: str):
    message = Messages.objects(id=ObjectId(message_id))
    if message.first().sender_id != user_id:
        return
    message.update(active=False)

    return True


def get_user_id_by_message(message_id: str):
    return Messages.objects(id=ObjectId(message_id)).first().sender_id


def get_last_message(room_id: str):
    message = Messages.objects(room_id=room_id, active=True).order_by('-created_at').first()
    if message:
        return message.to_dict()
    return {}


def get_unread_messages(room_id: str):
    return Messages.objects(room_id=room_id, seen=False, active=True)
