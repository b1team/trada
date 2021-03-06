from src.services.crud import users
from fastapi import APIRouter
from ..basemodels import User, User_update

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/users/{username}", tags=["user"])
def get_user_profile(username:str):
    if username is None:
        username = "vuonglv"
    user = users.get_user(username)
    if user is not None:
        return user

    return {'success': False}


@router.post("/users/", tags=["user"])
def create_user(user: User):
    username = user.username
    password = user.password
    new_user = users.create_user(username, password)
    if new_user:
        return {"success": True}

    return {"success": False}


@router.put("/users", tags=["user"])
def update_user(user: User_update):
    username = user.username
    password = user.password
    avatar = user.avatar_url
    name = user.name
    new_user_info = users.update_user(username, password, avatar, name)
    if new_user_info:
        return {'success': True}

    return {"success": False}


@router.delete("/users/{username}", tags=["user"])
def delete_user(username:str):
    if username is None:
        username = "vuonglv"
    user_delete = users.delete_user(username)
    if user_delete:
        return {'success': True}

    return {"success": False}