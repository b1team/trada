from . import schemas
from fastapi import APIRouter
from src.services.auth import AuthService, AdminAuthService
from src.api.exceptions import UnauthenticatedError
from src.config import settings

router = APIRouter(tags=["auth"])


@router.post("/token", response_model=schemas.Token)
def get_token(body: schemas.GetTokenBody):
    auth = AuthService(settings.TOKEN_SECRET_KEY)
    user = auth.authenticate_user(body.username, body.password)
    if not user:
        raise UnauthenticatedError("Username or password is incorrect")
    if not user.active:
        raise UnauthenticatedError("User was blocked")
    data = {"username": user.username, "user_id": str(user.id)}
    access_token = auth.create_access_token(
        data=data, token_duration=settings.TOKEN_DURATION)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/admin/token", response_model=schemas.Token)
def get_admin_token(body: schemas.GetTokenBody):
    auth = AdminAuthService(settings.ADMIN_TOKEN_SECRET_KEY)
    user = auth.authenticate_user(body.username, body.password)
    if not user:
        raise UnauthenticatedError("Username or password is incorrect")
    if not user.active:
        raise UnauthenticatedError("User was blocked")
    data = {"username": user.username, "user_id": str(user.id)}
    access_token = auth.create_access_token(
        data=data, token_duration=settings.TOKEN_DURATION)
    return {"access_token": access_token, "token_type": "bearer"}
