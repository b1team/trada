from typing import Any, Dict

import jwt
from fastapi import Header
from fastapi.param_functions import Depends
from src.api.exceptions import UnauthenticatedError
from src.config import settings
from src.services.crud.users.logic import get_user


async def get_token_payload(bearer_token: str = Header(..., alias="Authorization")
) -> Dict[str, Any]:
    if not bearer_token.startswith("Bearer "):
        raise UnauthenticatedError("Header token missing Bearer")
    _, _, token = bearer_token.partition("Bearer ")
    if not token:
        raise UnauthenticatedError("Header token missing access_token")
    try:
        decoded = jwt.decode(token, settings.TOKEN_SECRET_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError as ex:
        raise UnauthenticatedError("Token invalid")
    else:
        return decoded

async def get_current_user(token_payload: Dict[str, Any] = Depends(get_token_payload)):
    user = get_user(token_payload["username"])
    if not user:
        raise UnauthenticatedError("Invalid User")
    return user
