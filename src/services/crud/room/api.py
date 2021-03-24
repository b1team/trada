from . import logic
from src.api.exceptions import room_errors


def create_room(room_name: str, user_id: str):
    if logic.check_room_exists(room_name):
        raise room_errors.ExistingError(obj=f"Room {room_name}")

    room = logic.create_room(room_name)
    owner = logic.invite_member(room.room_id, user_id, is_owner=True)

    data = {
        "room": room.to_dict(),
        "owner": owner.to_dict()
    }

    return data


def invite_member(room_id: str, member_id: str):
    try:
        member = logic.check_member_exists(room_id, member_id)
    except:
        raise room_errors.IdFormatError()
    if member:
        raise room_errors.ExistingError(obj=f"Member {member_id}")

    return logic.invite_member(room_id, member_id)


def delete_room(room_id: str):
    try:
        room = logic.check_room_exists(room_id)
    except:
        raise room_errors.IdFormatError()
    if room:
        return logic.remove_room(room_id)

    return False


def delete_member(room_id: str, member_id: str):
    return logic.remove_member(room_id, member_id)