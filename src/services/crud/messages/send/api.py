from ...users.logic import check_user_exist
from ...groups.group.logic import check_group_exists
from .logic import (send_group,
                    send_private)
import datetime

def send_message(content, senderId, sendername, recivedname):
    is_group = check_group_exists(recivedname)
    is_user = check_user_exist(recivedname)

    if is_user:
        send_to_user = send_private(content, senderId, sendername, recivedname)

        return {"success":send_to_user,
                "from": sendername,
                "content": content,
                "send_at": datetime.datetime.utcnow}

    if is_group:
        send_to_group = send_group(content, senderId, sendername, recivedname)

        return {"success":send_to_group,
                "from": sendername,
                "content": content,
                "send_at": datetime.datetime.utcnow}