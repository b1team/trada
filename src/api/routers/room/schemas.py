from typing import Optional

from pydantic import BaseModel


class BasicSchemas(BaseModel):
    room_id: Optional[str] = None
    member_id: Optional[str] = None
