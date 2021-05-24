from typing import Optional

from src.api.exceptions import internal_errors, user_errors

from . import logic


def create_user(
    username: str,
    password: str,
    name: str,
):
    if (username and password and name == "") == "":
        return
    existing_user = logic.get_user(username)
    if existing_user:
        raise user_errors.ExistingError(obj=f"User {username}")
    return logic.save_user(username, password, name=name)


def get_user(username: str):
    existing_user = logic.get_user(username)
    if existing_user:
        return logic.get_user(username)
    else:
        raise user_errors.NotFoundError(obj=f"User {username}")


def update_user(user_id: str,
                username: str,
                avatar: Optional[str] = None,
                name: Optional[str] = None):
    existing_user = logic.get_user_by_id(user_id)
    if existing_user:
        try:
            user_update = logic.update_current_user(user_id, username, avatar,
                                                    name)
        except:
            raise internal_errors.InternalError(detail="Could not update user")
        return user_update
    else:
        raise user_errors.NotFoundError(obj=f"User {user_id}")


def delete_user(username: str):
    existing_user = logic.get_user(username)
    if existing_user:
        return logic.disabe_user(username)
    else:
        raise user_errors.NotFoundError(obj=f"User {username}")
