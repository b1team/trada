from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from mongoengine import connect, disconnect
from src.config import settings
from starlette.routing import Host

from .routers import messages, send_message, users

app = FastAPI()

app.include_router(users.router)
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
