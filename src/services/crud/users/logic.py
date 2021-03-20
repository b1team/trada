from typing import Optional

from bson import ObjectId
from src.libs.models.users import User


def check_user_exist(user_id):
    user = User.objects(id=ObjectId(user_id)).first()
    if user:
        return True
    return False


def get_user(username: str):
    return User.objects(username=username).first()


def save_user(
    username: str,
    password: str
):
    user = User(username=username, password=password)
    return user.save()


def get_user_profile(username):
    user = User.objects(username=username).first()

    return user.to_json()


def update_current_user(
    username: str,
    avatar: Optional[str] = None,
    name: Optional[str] = None,
):
    user = User.objects(username=username)
    fileds = {
        "avatar": avatar,
        "name": name,
    }
    user.update(**fileds)

    return True


def remove_user(username):
    user = User.objects(username=username)
    user.delete()

    return True
