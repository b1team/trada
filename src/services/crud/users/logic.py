from typing import Optional
from src.libs.models.users import User


def check_user_exist(username):
    user = User.objects(username=username).first()
    if user:
        return True
    return False


def get_user(username: str):
    return User.objects(username=username).first()


def save_user(
    username: str,
    password: str,
    name: Optional[str] = None,
    avatar: Optional[str] = None,
):
    user = User(username=username, password=password, name=name, avatar=avatar)
    return user.save()


def get_user_profile(username):
    user = User.objects(username=username).first()

    return user.to_json()


def update_current_user(username, password, avatar, name):
    user = User.objects(username=username)
    fileds = {
        "username": username,
        "password": password,
        "avatar": avatar,
        "name": name,
    }
    user.update(**fileds)
    user.reload()

    return True


def remove_user(username):
    user = User.objects(username=username)
    user.delete()

    return True