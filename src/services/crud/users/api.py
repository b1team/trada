from typing import Optional

from src.api.exceptions import internal_errors, user_errors

from . import logic


def create_user(
    username: str,
    password: str,
    name: Optional[str] = None,
    avatar: Optional[str] = None,
):
    existing_user = logic.get_user(username)
    if existing_user:
        raise user_errors.ExistingError(obj=f"User {username}")
    return logic.save_user(username, password, name, avatar)


def get_user(username: str):
    existing_user = logic.get_user(username)
    if existing_user:
        return logic.get_user(username)
    else:
        raise user_errors.NotFoundError(obj=f"User {username}")


def update_user(username: str,
                avatar: Optional[str] = None,
                name: Optional[str] = None):
    existing_user = logic.get_user(username)
    if existing_user:
        try:
            user_update = logic.update_current_user(username, avatar, name)
        except:
            raise internal_errors.InternalError(detail="Could not update user")
        return user_update
    else:
        raise user_errors.NotFoundError(obj=f"User {username}")


def delete_user(username: str):
    existing_user = logic.get_user(username)
    if existing_user:
        return logic.remove_user(username)
    else:
        raise user_errors.NotFoundError(obj=f"User {username}")
