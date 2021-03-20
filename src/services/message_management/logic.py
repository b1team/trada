from typing import Optional

from src.services.crud.messages.message import save_message


def send_private(content: str,
                 sender_id: Optional[str] = None,
                 receiver_id: Optional[str] = None):
    message = save_message(content, sender_id, receiver_id)

    return message