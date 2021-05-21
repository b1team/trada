from typing import Optional
from src.services.crud.users import logic as user_logic
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
    try:
        users = logic.users_load()
    except:
        print("Loading users failed")

    return users


def get_admin(username: str):
    existing_user = logic.get_user(username)
    if existing_user:
        return logic.get_user(username)
    else:
        raise user_errors.NotFoundError(obj=f"User {username}")


def update_admin(user_id: str,
                 username: str,
                 avatar: Optional[str] = None,
                 name: Optional[str] = None):
    existing_user = logic.get_user_by_id(user_id)
    if existing_user:
        try:
            user_update = logic.update_current_admin(user_id, username, avatar,
                                                     name)
        except:
            raise internal_errors.InternalError(detail="Could not update user")
        return user_update
    else:
        raise user_errors.NotFoundError(obj=f"User {user_id}")


def disable_user(user_id: str):
    try:
        user_disable = logic.user_disable(user_id)
    except:
        raise user_errors.IdFormatError()

    return user_disable


def create_room(room_name: str, user_id: str):
    if logic.get_room(room_name):
        raise room_errors.ExistingError(obj=f"Room {room_name}")
    user = logic.get_user_by_id(user_id)
    room = logic.room_create(room_name)
    room_logic.invite_member(room.id, user.username, is_owner=True)

    data = {
        "room": room.to_dict(),
        "owner": user.to_dict(),
    }

    return data


def load_rooms():
    try:
        rooms = logic.rooms_load()
    except:
        print("Loading rooms failed")
    return rooms


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
    try:
        mess = logic.total_messages(start_time, end_time)
    except:
        print("Messages error")
    return mess


def create_admin(
    username: str,
    password: str,
    name: str,
):
    existing_user = logic.get_user(username)
    if existing_user:
        raise user_errors.ExistingError(obj=f"User {username}")
    return logic.save_user(username, password, name)
