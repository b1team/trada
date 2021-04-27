from typing import Optional
from src.services.crud.users import logic as user_logic
from src.services.crud.messages import logic as message_logic
from src.services.crud.room import logic as room_logic
from src.api.exceptions import internal_errors, user_errors, room_errors
from . import logic


def create_user(
    username: str,
    password: str,
    name: str,
):
    existing_user = user_logic.get_user(username)
    if existing_user:
        raise user_errors.ExistingError(obj=f"User {username}")

    return logic.user_create(username, password, name)


def load_users():
    users = logic.users_load()

    return users


def disable_user(user_id: str):
    try:
        user_disable = logic.user_disable(user_id)
    except:
        raise  user_errors.IdFormatError()

    return user_disable


def create_room(room_name: str, user_id: str):
    if logic.get_room(room_name):
        raise room_errors.ExistingError(obj=f"Room {room_name}")
    user = user_logic.get_user_by_id(user_id)
    room = logic.room_create(room_name)
    room_logic.invite_member(room.id, user.username, is_owner=True)

    data = {
        "room": room.to_dict(),
        "owner": user.to_dict(),
    }

    return data


def load_rooms():
    return logic.rooms_load()


def remove_room(room_id: str):
    try:
        room = room_logic.check_room_exists(room_id)
    except:
        raise room_errors.IdFormatError()
    if room:
        return logic.room_delete(room_id)

    return False


def messages_count(start_time: Optional[str] = None,
                   end_time: Optional[str] = None):
    return logic.total_messages(start_time, end_time)