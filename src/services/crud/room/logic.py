from src.libs.models.room_member import RoomMember
from src.libs.models.room import Room
from src.libs.models.message import Messages
from src.libs.models.users import User
from src.services.crud.messages import logic
from src.services.crud.users import logic as user_logic
from bson import ObjectId
from typing import Optional
from dateutil.parser import parse


def check_room_exists(room_id: str):
    room = Room.objects(id=ObjectId(room_id)).first()
    if room:
        return True
    return False


def get_room(room_name: str):
    return Room.objects(room_name=room_name).first()


def check_member_exists(room_id: str, member_id: str):
    member = RoomMember.objects(room_id=room_id, member_id=member_id).first()
    if member:
        return True
    return False


def create_room(room_name: str):
    room = Room(room_name=room_name)

    return room.save()


def invite_member(room_id: str,
                  member_name: str,
                  is_owner: Optional[bool] = False):
    filters = dict()

    if room_id:
        filters.update({'room_id': str(room_id)})
    if member_name:
        member_id = user_logic.get_user_id(member_name)
        filters.update({'member_id': str(member_id)})
    if is_owner:
        filters.update({'is_owner': is_owner})

    member = RoomMember(**filters)

    return member.save()


def remove_room(room_id: str):
    room = Room.objects(id=ObjectId(room_id)).first()
    member = RoomMember.objects(room_id=room_id)
    messages = Messages.objects(room_id=room_id)
    room.delete()
    member.delete()
    messages.delete()

    return True


def remove_member(room_id: str, member_name: str):
    user = user_logic.get_user(member_name)
    member = RoomMember.objects(room_id=room_id, member_id=str(user.id)).first()
    member.delete()

    return str(user.id)


def room_members(room_id: str):
    members = RoomMember.objects(room_id=room_id)
    list_members = []
    for member in members:
        list_members.append(member.member_id)

    return list_members


def check_is_member(room_id: str, member_id: str):
    owner = RoomMember.objects(room_id=room_id, member_id=member_id).first()
    if not owner:
        return False
    if owner.is_owner:
        return False
    else:
        return True


def check_is_admin(room_id: str, member_id: str):
    owner = RoomMember.objects(room_id=room_id, member_id=member_id).first()
    if not owner:
        return
    if owner.is_owner:
        return True
    return False


def get_user_room(user_id: str):
    in_room = RoomMember.objects(member_id=user_id)
    if not in_room:
        return {"detail": "No room success"}
    list_rooms = []
    for info in in_room:
        room = Room.objects(id=ObjectId(info.room_id)).first()
        data = room.to_dict()
        last_message = logic.get_last_message(info.room_id)
        try:
            last_message['timestamp'] = parse(
                last_message['created_at']).strftime('%d %b,%Y %H:%M')
        except:
            pass
        data['last_message'] = last_message
        data['unreadCount'] = len(logic.get_unread_messages(info.room_id))
        list_rooms.append(data)

    return list_rooms


def get_room_info(room_id: str):
    room = Room.objects(id=ObjectId(room_id)).first()
    if room:
        return {
            "id": str(room.id),
            "type": room.type,
            "room_name": room.room_name,
            "display_name": room.display_name,
            "avatar": room.avatar,
        }
    return None


def update_room(room_id: str, room_name: str, avatar: str):
    room = Room.objects(id=ObjectId(room_id))
    filters = {
        "room_name": room_name,
        "avatar": avatar,
    }

    room.update(**filters)

    return True


def get_members(room_id: str):
    members_id = RoomMember.objects(room_id=room_id)

    list_members = []
    for member in members_id:
        user = User.objects(id=ObjectId(member.member_id)).first()
        _user = user.to_dict()
        _user["is_owner"] = member.is_owner
        list_members.append(_user)

    return list_members
