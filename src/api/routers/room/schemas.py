from typing import Optional

from pydantic import BaseModel


class BasicSchemas(BaseModel):
    room_id: Optional[str] = None
    member_name: Optional[str] = None


class UpdateRoomSchemas(BaseModel):
    room_id: Optional[str] = None
    room_name: Optional[str] = None
    avatar: Optional[str] = None