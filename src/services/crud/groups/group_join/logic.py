from src.libs.models.groups_join import Group_members


def join_group(member_name: str, group_name: str):
    join = Group_members(member_name=member_name, group_name=group_name)
    return join.save()
