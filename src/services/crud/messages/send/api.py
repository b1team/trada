from src.services.crud.users.logic import get_user
from src.services.crud.groups.group.logic import get_group
from .logic import (send_group,
                    send_private)
from datetime import datetime
from typing import Optional
from src.api.exceptions import user_errors

def send_message(
    content: str,
    senderId: Optional[str] = None,
    sendername: Optional[str] = None,
    recivedname: Optional[str] = None
):
    is_group = get_group(recivedname)
    is_user = get_user(recivedname)

    if not (is_group or is_user):
        raise user_errors.NotFoundError(obj=f"Reciver {recivedname}")

    sender_exist = get_group(sendername) or get_user(sendername)
    if not sender_exist:
        raise user_errors.NotFoundError(obj=f"Sender {sendername}")

    if is_user:
        send_to_user = send_private(content, senderId, sendername, recivedname)

        return {"success":f"send to user {sendername}",
                "from": sendername,
                "content": content,
                "send_at": str(datetime.utcnow())}

    if is_group:
        send_to_group = send_group(content, senderId, sendername, recivedname)

        return {"success": f"send to group {sendername}",
                "from": sendername,
                "content": content,
                "send_at": str(datetime.utcnow())}

    return False