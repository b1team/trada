from fastapi.exceptions import HTTPException
from src.services.crud.groups import group
from fastapi import APIRouter
from . import schemas

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/groups/{group_name}", tags=["groups"])
def get_group_profile(group_name:str):
    if group_name is None:
        group_name = "vuonglv"
    get_group = group.get_group(group_name)
    if get_group is not None:
        return get_group

    return {"success": False}


@router.post("/groups", response_model=schemas.CreateGroupResponseSchema)
def create_group(group_new: schemas.CreateGroupSchema):
    if (group_new.group_name or group_new.user_created) is None:
        raise HTTPException(status_code=404, detail="Please enter details of group")
    Group = group.create_group(
        group_name=group_new.group_name,
        user_created=group_new.user_created)

    return Group.to_dict()


@router.put("/groups", tags=["groups"])
def update_group():
    group_name = "vuonglv" #thay = id sau :v
    avatar = "https://defaultavatr.com"
    group_update = group.update_group(group_name, avatar)
    if group_update:
        return {"success": True}

    return {"success": False}


@router.delete("/groups/{group_name}", tags=["groups"])
def delete_group(group_name:str):
    if group_name is None:
        group_name = "vuonglv"
    group = group.delete_group(group_name)
    if group:
        return {"success": True}

    return {"success": False}