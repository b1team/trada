from typing import Optional

from src.api.exceptions import user_errors
from src.services.crud.users.logic import get_user

from . import logic


def create_group(group_name: str, user_created: str):
    group_exist = logic.get_group(group_name)
    user_exist = get_user(user_created)
    if group_exist:
        raise user_errors.ExistingError(obj=f"Group {group_name}")
    if not user_exist:
        raise user_errors.NotFoundError(obj=f"User {user_created}")
    return logic.save_group(group_name, user_created)


def get_group(group_name: str):
    group_exist = logic.get_group(group_name)
    if not group_exist:
        raise user_errors.NotFoundError(obj=f"Group {group_name}")
    return logic.get_group(group_name)


def update_group(group_name: str, group_avatar: Optional[str] = None):
    group_exist = logic.get_group(group_name)
    if not group_exist:
        raise user_errors.NotFoundError(obj=f"Group {group_name}")
    return logic.update_group_profile(group_name, group_avatar)


def delete_group(group_name: str):
    group_exist = logic.get_group(group_name)
    if not group_exist:
        raise user_errors.NotFoundError(obj=f"Group {group_name}")
    return logic.delete_group(group_name)
