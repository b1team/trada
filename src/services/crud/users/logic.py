from typing import Optional

from bson import ObjectId
from src.libs.models.users import User


def check_user_exist(user_id: str):
    user = User.objects(id=ObjectId(user_id)).first()
    if user:
        return True
    return False


def get_user_by_id(user_id: str):
    return User.objects(id=ObjectId(user_id)).first()


def get_user(username: str):
    return User.objects(username=username).first()


def get_public_user_info(user_id: str):
    user = User.objects(id=ObjectId(user_id)).first()
    if user:
        return {
            "username": user.username,
            "name": user.name,
            "user_id": str(user.id),
            "avatar": user.avatar,
        }
    return None


def save_user(username: str, password: str, name: str):
    user = User(username=username, password=password, name=name)
    return user.save()


def get_user_profile(username: str):
    user = User.objects(username=username).first()

    return user.to_dict()


def update_current_user(
    user_id: str,
    username: str,
    avatar: Optional[str] = None,
    name: Optional[str] = None,
):
    user = User.objects(id=ObjectId(user_id))
    fileds = {
        "username": username,
        "avatar": avatar,
        "name": name,
    }
    user.update(**fileds)

    return True


def disabe_user(username: str):
    user = User.objects(username=username).first()
    user.update(active=False)

    return True


def check_user_active(username: str):
    active = User.objects(username=username).first().active
    if active:
        return True

    return False


def get_user_id(username: str):
    user_id = User.objects(username=username).first().id
    if user_id:
        return user_id
    return False