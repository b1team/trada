from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from src.services.crud import users

from . import schemas

router = APIRouter(tags=["user"])


@router.get("/users/{username}", response_model=None)
def get_user_profile(username: str):
    if username is None:
        raise HTTPException(status_code=404, detail="Please enter username")
    user = users.get_user(username)
    return user.to_dict()


@router.post("/users", response_model=schemas.CreateUserResponseSchema)
def create_user(user: schemas.CreateUserSchema):
    new_user = users.create_user(
        username=user.username,
        password=user.password,
        name=user.name,
        avatar=user.avatar,
    )
    return new_user.to_dict()


@router.put("/users", tags=["user"])
def update_user(user):
    username = user.username
    password = user.password
    avatar = user.avatar_url
    name = user.name
    new_user_info = users.update_user(username, password, avatar, name)
    if new_user_info:
        return {"success": True}

    return {"success": False}


@router.delete("/users/{username}", tags=["user"])
def delete_user(username: str):
    if username is None:
        username = "vuonglv"
    user_delete = users.delete_user(username)
    if user_delete:
        return {"success": True}

    return {"success": False}
