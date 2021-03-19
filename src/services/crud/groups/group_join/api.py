from .logic import join_group
from ..group.logic import check_group_exists
from src.services.crud.users.logic import check_user_exist 


def to_join_group(member_name, group_name):
    user_exist = check_user_exist(member_name)
    group_exist = check_group_exists(group_name)
    if user_exist and group_exist:
        join = join_group(member_name, group_name)
        return join

    return False