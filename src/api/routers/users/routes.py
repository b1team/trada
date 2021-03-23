from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.services.crud import users

from . import schemas

router = APIRouter(tags=["user"])


@router.get("/users/{username}",
            response_model=schemas.UserProfileResponseSchema)
def get_user_profile(username: str):
    if username.strip() == "":
        raise HTTPException(status_code=404,
                            detail="Username must not be space")
    user = users.get_user(username)

    return user.to_dict()


@router.post("/users", response_model=schemas.CreateUserResponseSchema)
def create_user(user: schemas.CreateUserSchema):
    new_user = users.create_user(username=user.username,
                                 password=user.password,
                                 name=user.name)

    return new_user.to_dict()


@router.put("/users/{username}",
            response_model=schemas.UpdateUserResponseSchema)
def update_user(username: str, user: schemas.UpdateUserSchema):
    if username.strip() == "":
        raise HTTPException(status_code=404,
                            detail="Username must not be space")
    new_user_info = users.update_user(username, user.avatar, user.name)
    if new_user_info:
        return user


@router.delete("/users/{username}", response_model=schemas.BasicResponse)
def delete_user(username: str):
    if username.strip() == "":
        raise HTTPException(status_code=404,
                            detail="Username must not be space")
    user_delete = users.delete_user(username)
    if user_delete:
        return {"success": True}

    return {"success": False}
