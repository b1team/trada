from typing import Optional
from . import logic
from src.api.exceptions import user_errors


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
    user_exist = check_user_exist(username)
    if user_exist:
        user = get_user_profile(username)
        return user

    return False


def update_user(username: str, password: str, avatar: str, name: str):
    user_exist = check_user_exist(username)
    if user_exist:
        user_update = update_current_user(username, password, avatar, name)
        return user_update

    return False


def delete_user(username: str):
    user_exist = check_user_exist(username)
    if user_exist:
        delete_user = delete_current_user(username)
        return delete_user

    return False