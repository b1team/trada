from typing import Optional
from src.services.crud.messages import save_message


def send_to_user(content: str,
         sender_id: Optional[str] = None,
         room_id: Optional[str] = None):
    message = save_message(content, sender_id, room_id)

    return message