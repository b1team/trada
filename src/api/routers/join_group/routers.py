from src.services.crud.groups import group_join
from fastapi import APIRouter
from . import schemas
from fastapi.exceptions import HTTPException


router = APIRouter(prefix="/join_group", tags=["join_group"])

@router.post("/join/", response_model=schemas.JoinGroupResponseSchema)
def join_group(group_member: schemas.JoinGroupSchema):
    if (group_member.group_name or group_member.member_name) is None:
        raise HTTPException(status_code=404, detail="Please enter group name or member")

    group = group_join.to_join_group(
        group_member.member_name,
        group_member.group_name)
    if group:
       return group.to_dict()