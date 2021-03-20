from typing import Optional

from src.libs.models.groups_join import Group_members
from src.services.crud.messages.message import save_message


def send_private(content: str,
                 sender_id: Optional[str] = None,
                 receiver_id: Optional[str] = None):
    message = save_message(content, sender_id, receiver_id)

    return message


def send_group(content: str,
               senderId: Optional[str] = None,
               sendername: Optional[str] = None,
               recivedname: Optional[str] = None):
    members = Group_members.objects(group_name=recivedname, left=False)
    list_members = []
    for member in members:
        list_members.append(member.member_name)

    for member in range(len(list_members)):
        save_message(content, senderId, sendername, list_members[member])

    return True
