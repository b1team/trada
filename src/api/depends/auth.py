from src.libs.models.users import User
from typing import Any, Dict, Union

import jwt
from fastapi import Header, WebSocket, status
from fastapi.param_functions import Depends, Query
from src.api.exceptions import UnauthenticatedError
from src.config import settings
from src.services.crud.users.logic import get_user


async def get_token_payload(bearer_token: str = Header(
    None, alias="Authorization")) -> Dict[str, Any]:
    if not bearer_token.startswith("Bearer "):
        raise UnauthenticatedError("Header token missing Bearer")
    _, _, token = bearer_token.partition("Bearer ")
    if not token:
        raise UnauthenticatedError("Header token missing access_token")
    try:

        decoded = jwt.decode(
            token, settings.TOKEN_SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError as ex:
        raise UnauthenticatedError("Given token was expired")
    else:
        return decoded


async def get_token_payload_ws(token: str = Query(...)) -> Dict[str, Any]:
    if not token:
        return {"success": False, "payload": {}}
    try:
        decoded = jwt.decode(
            token, settings.TOKEN_SECRET_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError as ex:
        return {"success": False, "payload": {}}
    else:
        return {"success": True, "payload": decoded}



async def get_current_user(
        token_payload: Dict[str, Any] = Depends(get_token_payload)):
    user = get_user(token_payload["username"])
    if not user:
        raise UnauthenticatedError("Invalid User")
    return user


async def get_current_user_ws(
    websocket: WebSocket,
    get_token_result: Dict[str, Any] = Depends(get_token_payload_ws)
) -> Union[None, User]:
    success = get_token_result.get("success", False)
    if not success:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    payload = get_token_result.get("payload", {})
    if not payload:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    username = payload.get("username", "")
    if not username:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    user = get_user(username=username)
    if not user:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    return user
