from .logic import join_group
from src.services.crud.groups.group.logic import check_group_exists
from src.services.crud.users.logic import get_user
from src.api.exceptions import user_errors

def to_join_group(member_name: str, group_name: str):
    user_exist = get_user(member_name)
    if not user_exist:
        raise user_errors.NotFoundError(obj=f"User {member_name}")

    group_exist = check_group_exists(group_name)
    if not group_exist:
        raise user_errors.NotFoundError(obj=f"Group {group_name}")

    return join_group(member_name, group_name)