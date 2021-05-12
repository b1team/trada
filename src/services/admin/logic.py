from re import S
from typing import Optional

from bson import ObjectId
from dateutil.parser import parse
from src.libs.models.message import Messages
from src.libs.models.room import Room
from src.libs.models.room_member import RoomMember
from src.libs.models.users import User
from src.services.crud.messages import logic as mess_logic


# USER
def user_create(username: str, password: str, name: str):
    username = username.strip()
    password = password.strip()
    name = name.strip()

    if (username and password and name) == "":
        return {"detail": "data empty"}

    new_user = User(username=username, password=password, name=name)

    return new_user.save()


def users_load():
    users = User.objects()
    list_users = []
    for user in users:
        list_users.append(user.to_dict())

    return list_users


def user_disable(user_id: str):
    user = User.objects(id=ObjectId(user_id)).first()
    active = not user.active
    user.update(active=active)

    return True


# ROOM
def room_create(room_name: str):
    room_name = room_name.strip()
    if room_name == "":
        return {"detail": "room name must not be empty"}
    room = Room(room_name=room_name)

    return room.save()


def rooms_load():
    rooms = Room.objects()
    list_rooms = []
    for room in rooms:
        members = RoomMember.objects(room_id=str(room.id))
        messages_count = Messages.objects(room_id=str(room.id)).count()
        _room = room.to_dict()
        last_message = mess_logic.get_last_message(str(room.id))
        try:
            last_message['timestamp'] = parse(
                last_message['created_at']).strftime('%d %b,%Y %H:%M')
        except:
            pass
        _room['last_message'] = last_message
        _room["member"] = []
        _room["messages_count"] = messages_count
        for member in members:
            user = User.objects(id=ObjectId(member.member_id)).first()
            _room["member"].append(user.to_dict())
        list_rooms.append(_room)

    return list_rooms


def room_delete(room_id: str):
    room = Room.objects(id=ObjectId(room_id)).first()
    member = RoomMember.objects(room_id=room_id)
    messages = Messages.objects(room_id=room_id)
    room.delete()
    member.delete()
    messages.delete()

    return True


# MESSAGES
def total_messages(start_time: Optional[str] = None,
                   end_time: Optional[str] = None):
    filters = dict()
    if start_time:
        filters.update({"created_at__gte": start_time})
    if end_time:
        filters.update({"created_at__lte": end_time})

    messages_count = Messages.objects(**filters).count()

    return messages_count
