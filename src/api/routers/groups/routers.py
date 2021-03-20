from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.services.crud.groups import group

from . import schemas

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/groups/{group_name}", response_model=None)
def get_group_profile(group_name: str):
    if group_name is None:
        raise HTTPException(status_code=404,
                            detail="Please enter a group name")
    Group = group.get_group(group_name)

    return Group.to_dict()


@router.post("/groups", response_model=schemas.CreateGroupResponseSchema)
def create_group(group_new: schemas.CreateGroupSchema):
    if (group_new.group_name or group_new.user_created) is None:
        raise HTTPException(status_code=404,
                            detail="Please enter details of group")
    Group = group.create_group(group_name=group_new.group_name,
                               user_created=group_new.user_created)

    return Group.to_dict()


@router.put("/groups", response_model=None)
def update_group(new_update: schemas.UpdateGroupSchema):
    if (new_update.group_name or new_update.avatar) is None:
        raise HTTPException(status_code=404,
                            detail="Please enter details of new group")
    group_update = group.update_group(new_update.group_name, new_update.avatar)
    if group_update:
        return {f"Group {new_update.group_name} has been updated."}
    return {"success": False}


@router.delete("/groups/{group_name}", response_model=None)
def delete_group(group_name: str):
    if group_name is None:
        raise HTTPException(status_code=404,
                            message="Please enter a group name")
    group_delete = group.delete_group(group_name)
    if group_delete:
        return {f"Group {group_name} has been deleted"}
    return {"success": False}
