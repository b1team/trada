from ...messages.message import save
from src.libs.models.groups_join import Group_members

def send_private(content, senderId, sendername, recivedname):
    message = save(content, senderId, sendername, recivedname)

    return message


def send_group(content, senderId, sendername, recivedname):
    members = Group_members.objects(group_name=recivedname, left=False)
    list_members = []
    for member in members:
        list_members.append(member.member_name)

    for member in range(len(list_members)):
        save(content, senderId, sendername, list_members[member])

    return True