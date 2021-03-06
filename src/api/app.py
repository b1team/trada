from src.services.crud import groups
from fastapi import FastAPI
from .routers import users
from .routers import groups
from .routers import join_group
from .routers import messages
from .routers import send_message

app = FastAPI()

app.include_router(users.router)
app.include_router(groups.router)
app.include_router(join_group.router)
app.include_router(messages.router)
app.include_router(send_message.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
