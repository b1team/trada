from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from src.services.crud import users
from src.services.crud.users.logic import get_user

from . import schemas

router = APIRouter(tags=["user"])


@router.get("/users/{username}", response_model=schemas.UserProfileResponseSchema)
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


@router.put("/users/{username}", response_model=schemas.UpdateUserResponseSchema)
def update_user(
    username: str,
    user: schemas.UpdateUserSchema
):
    new_user_info = users.update_user(
        username,
        user.avatar,
        user.name
        )
    if new_user_info:
        return user



@router.delete("/users/{username}", response_model=schemas.BasicResponse)
def delete_user(username: str):
    user_delete = users.delete_user(username)
    if user_delete:
        return {"info": f"User {username} has been deleted"}
    return {"success": False}
