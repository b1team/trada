from . import logic
from src.api.exceptions import user_errors
from src.services.crud.users.logic import get_user


def create_group(
    group_name:str,
    user_created:str
):
    group_exist = logic.get_group(group_name)
    user_exist = get_user(user_created)
    if group_exist:
        raise user_errors.ExistingError(obj=f"Group {group_name}")
    if not user_exist:
        raise user_errors.NotFoundError(obj=f"User {user_created}")
    return logic.save_group(group_name, user_created)


def get_group(group_name:str):
    group_exist = check_group_exists(group_name)
    if group_exist:
        group = get_group_profile(group_name)
        return group

    return False


def update_group(group_name:str, group_avatar:str):
    group_exist = check_group_exists(group_name)
    if group_exist:
        group = update_group_profile(group_name, group_avatar)
        return group

    return False


def delete_group(group_name:str):
    group_exist = check_group_exists(group_name)
    if group_exist:
        group = destroy_group(group_name)
        return group

    return False