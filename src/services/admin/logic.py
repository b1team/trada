from re import S
from typing import Optional

from bson import ObjectId
from dateutil.parser import parse
from src.libs.models.message import Messages
from src.libs.models.room import Room
from src.libs.models.room_member import RoomMember
from src.libs.models.users import User
from src.services.crud.messages import logic as mess_logic
from src.libs.models.admin import Admin


# USER
def user_create(username: str, password: str, name: str):
    user = User(username=username, password=password, name=name)
    return user.save()


def get_user_by_id(user_id: str):
    return Admin.objects(id=ObjectId(user_id)).first()


def save_user(username: str, password: str, name: str):
    user = Admin(username=username, password=password, name=name)
    return user.save()


def get_user(username: str):
    return Admin.objects(username=username).first()


def users_load():
    users = User.objects()
    list_users = []
    for user in users:
        list_users.append(user.to_dict())

    return list_users[-5:]


def update_current_admin(
    user_id: str,
    username: str,
    avatar: Optional[str] = None,
    name: Optional[str] = None,
):
    user = Admin.objects(id=ObjectId(user_id))
    fileds = {
        "username": username,
        "avatar": avatar,
        "name": name,
    }
    user.update(**fileds)

    return True


def user_disable(user_id: str):
    user = User.objects(id=ObjectId(user_id)).first()
    active = not user.active
    user.update(active=active)

    return True


def user_delete(user_id: str):
    user = User.objects(id=user_id)
    members = RoomMember.objects(member_id=str(user_id))
    if not members:
        user.delete()
        return True
    for member in members:
        if member.is_owner:
            return False

    user.delete()
    member.delete()

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

    return list_rooms[-5:]


def room_delete(room_id: str):
    room = Room.objects(id=ObjectId(room_id)).first()
    member = RoomMember.objects(room_id=room_id)
    messages = Messages.objects(room_id=room_id)
    if not messages:
        room.delete()
        member.delete()
        return True

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
