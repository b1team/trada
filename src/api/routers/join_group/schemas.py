from pydantic import BaseModel
from datetime import datetime


class JoinGroupSchema(BaseModel):
    member_name: str
    group_name: str


class JoinGroupResponseSchema(BaseModel):
    group_id: str
    member_name: str
    group_name: str
    join_at: datetime
    left: bool