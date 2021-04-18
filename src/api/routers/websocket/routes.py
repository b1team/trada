import asyncio
import json
from typing import Union

import aioredis
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.param_functions import Depends
from src.api.depends.auth import get_current_user_ws
from src.config import settings
from src.libs.models.users import User
from src.logger import logger
from websockets.exceptions import ConnectionClosed

router = APIRouter(tags=["websocket"])


@router.websocket("/ws/chat")
async def chat(websocket: WebSocket,
               user: Union[None, User] = Depends(get_current_user_ws)):
    if not user:
        return
    user_id = str(user.id)
    await websocket.accept()
    redis = await aioredis.create_redis_pool(settings.REDIS_URI)
    response = await redis.subscribe(channel=user_id)
    channel = response[0]
    try:
        while await channel.wait_message():
            raw_event = await channel.get(encoding="utf8")
            try:
                event = json.loads(raw_event)
            except json.JSONDecodeError as e:
                logger.warning(
                    f"[{user_id}]Event '{raw_event}' was ignored. Decode failed"
                )
                continue
            else:
                await websocket.send_text(raw_event)
    except ConnectionClosed as e:
        logger.info(f"User {user_id} Disconnected")
    finally:
        redis.close()
        await redis.wait_closed()


@router.websocket("/ws/notifications")
async def notification(websocket: WebSocket,
              user: Union[None, User] = Depends(get_current_user_ws)):
    if not user:
        return
    user_id = str(user.id)
    await websocket.accept()
    redis = await aioredis.create_redis_pool(settings.REDIS_URI)
    response = await redis.subscribe(channel=f"{user_id}_notify")
    channel = response[0]
    try:
        while await channel.wait_message():
            raw_event = await channel.get(encoding="utf8")
            try:
                event = json.loads(raw_event)
            except json.JSONDecodeError as e:
                logger.warning(
                    f"[{user_id}]Event '{raw_event}' was ignored. Decode failed"
                )
                continue
            else:
                await websocket.send_text(raw_event)
    except ConnectionClosed as e:
        logger.info(f"User {user_id} Disconnected")
    finally:
        redis.close()
        await redis.wait_closed()

