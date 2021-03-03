from fastapi import FastAPI
from src.services.crud import users

app = FastAPI()


@app.get("/")
def hello():
    return {"ok": True}


@app.post("/users")
def create_user():
    username = "vuonglv"
    password = ""
    user_id = users.create_user(username, password)
    if user_id:
        return {"success": True}
    return {"success": False}
