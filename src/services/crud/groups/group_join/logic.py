from .models import Group_members


def join_group(member_name, group_name):
    join = Group_members(member_name=member_name, group_name=group_name)
    join.save()

    return True