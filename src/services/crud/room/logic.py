from src.libs.models.room_member import RoomMember
from src.libs.models.room import Room
from bson import ObjectId
from typing import Optional


def check_room_exists(room_id: str):
    room = Room.objects(id=ObjectId(room_id)).first()
    if room:
        return True
    return False


def check_member_exists(room_id: str, member_id: str):
    member = RoomMember.objects(room_id=room_id, member_id=member_id).first()
    if member:
        return True
    return False


def create_room(room_name: str):
    room = Room(room_name=room_name)

    return room.save()


def invite_member(room_id: Optional[str] = None,
                  member_id: Optional[str] = None,
                  is_owner: Optional[bool] = False):
    filters = {}

    if room_id:
        filter.update({'room_id': room_id})
    if member_id:
        filter.update({'member_id': member_id})
    if is_owner:
        filter.update({'is_owner': is_owner})

    member = RoomMember(**filters)

    return member.save()


def remove_room(room_id: str):
    room = Room.objects(id=ObjectId(room_id)).first()
    room.delete()

    return True


def remove_member(room_id: str, member_id: str):
    member = RoomMember.objects(room_id=room_id, member_id=member_id).first()
    member.delete()

    return True


def room_members(room_id: str):
    members = RoomMember.objects(room_id=room_id)
    list_members = []
    for member in members:
        list_members.append(member.member_id)

    return list_members