from src.services.crud.groups import group
from fastapi import APIRouter

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/groups/{group_name}", tags=["groups"])
def get_group_profile(group_name:str):
    if group_name is None:
        group_name = "vuonglv"
    get_group = group.get_group(group_name)
    if get_group is not None:
        return get_group

    return {"success": False}


@router.post("/groups/{group_name}/{user_create}", tags=["groups"])
def create_group(group_name:str, user_create:str):
    if group_name is None:
        group_name = "vuonglv"
    if user_create is None:
        user_create = "falcol"
    new_group = group.create_group(group_name, user_create)

    if new_group:
        return {"success": True}

    return {"success": False}


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