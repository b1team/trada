from .logic import (check_group_exists,
                    save_group,
                    destroy_group,
                    get_group_profile,
                    update_group_profile)


def create_group(group_name:str, user_created:str):
    group_exist = check_group_exists(group_name)
    if not group_exist:
        group = save_group(group_name, user_created)
        return group

    return False


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