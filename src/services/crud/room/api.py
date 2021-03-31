from . import logic
from src.api.exceptions import room_errors, user_errors
from src.services.crud.users.logic import get_user_by_id
from src.services.crud.users.logic import get_user_id


def create_room(room_name: str, user_id: str):
    if logic.get_room(room_name):
        raise room_errors.ExistingError(obj=f"Room {room_name}")
    user = get_user_by_id(user_id)
    avatar = user.avatar
    room = logic.create_room(room_name, avatar)
    owner = logic.invite_member(room.id, user.username, is_owner=True)

    data = {
        "room": room.to_dict(),
        "owner": user.to_dict(),
    }

    return data


def invite_member(room_id: str, member_name: str):
    try:
        member_id = get_user_id(member_name)
        if not member_id:
            raise user_errors.NotFoundError(obj=f"User {member_name}")
        member = logic.check_member_exists(room_id, member_id)
    except:
        raise room_errors.IdFormatError()
    if member:
        raise room_errors.ExistingError(obj=f"Member {member_name}")

    return logic.invite_member(room_id, member_name)


def delete_room(room_id: str):
    try:
        room = logic.check_room_exists(room_id)
    except:
        raise room_errors.IdFormatError()
    if room:
        return logic.remove_room(room_id)

    return False


def get_room_members(room_id: str):
    return logic.room_members(room_id)


def delete_member(room_id: str, member_name: str):
    return logic.remove_member(room_id, member_name)


def get_rooms(user_id: str):
    try:
        rooms = logic.get_user_room(user_id)
    except:
        raise room_errors.IdFormatError()

    return rooms