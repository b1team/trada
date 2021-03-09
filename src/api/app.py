from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.routing import Host
from src.config import settings
from mongoengine import connect, disconnect
from src.services.crud import groups

from .routers import groups, join_group, messages, send_message, users

app = FastAPI()

app.include_router(users.router)
app.include_router(groups.router)
app.include_router(join_group.router)
app.include_router(messages.router)
app.include_router(send_message.router)


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.on_event("startup")
def startup_event():
    connect(host=settings.DB_URI)


@app.on_event("shutdown")
def shutdown_event():
    disconnect()
