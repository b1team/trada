from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from src.api.depends.auth import get_current_user
from src.config import settings
from src.libs.models.users import User
from src.services.auth import AuthService
from src.services.crud import users

from . import schemas

router = APIRouter(tags=["user"])


@router.get("/users/me", response_model=schemas.UserProfileResponseSchema)
def get_me(user: User = Depends(get_current_user)):
    return user.to_dict()


@router.get("/users/{username}",
            response_model=schemas.UserProfileResponseSchema)
def get_user_profile(username: str, user: User = Depends(get_current_user)):
    if username.strip() == "":
        raise HTTPException(status_code=411,
                            detail="Username must not be space")
    _user = users.get_user(username)

    return _user.to_dict()


@router.post("/users", response_model=schemas.CreateUserResponseSchema)
def create_user(user: schemas.CreateUserSchema):
    auth = AuthService(settings.TOKEN_SECRET_KEY)
    hashed_password = auth.hash_password(user.password.strip())
    new_user = users.create_user(username=user.username.strip(),
                                 password=hashed_password,
                                 name=user.name.strip())

    return new_user.to_dict()


@router.put("/users", response_model=schemas.UpdateUserResponseSchema)
def update_user(user: schemas.UpdateUserSchema,
                auth_user: User = Depends(get_current_user)):
    if user.username.strip() == '':
        raise HTTPException(status_code=411, detail="Invalid username")
    new_user_info = users.update_user(str(auth_user.id), user.username.strip(),
                                      user.avatar.strip(), user.name.strip())
    if new_user_info:
        return user


@router.delete("/users/{username}", response_model=schemas.BasicResponse)
def delete_user(username: str, auth_user: User = Depends(get_current_user)):
    if username.strip() == "":
        raise HTTPException(status_code=411,
                            detail="Username must not be space")
    if auth_user.username != username:
        raise HTTPException(status_code=403, detail="Permission denied")
    user_delete = users.delete_user(username)
    if user_delete:
        return {"success": True}

    return {"success": False}
