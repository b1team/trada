from .models import User
# from src.libs.data_manager import DataManager


def check_user_exist(username):
    user = User.objects(username=username).first()
    if user:
        return True
    return False


def save_user(username, password):
    user = User(username=username, password=password)
    user.save()

    return True


def get_user_profile(username):
    user = User.objects(username=username).first()

    return user.to_json()


def update_current_user(username, password, avatar, name):
    user = User.objects(username=username)
    fileds = {
        'username': username,
        'password': password,
        'avatar': avatar,
        'name': name,
    }
    user.update(**fileds)
    user.reload()

    return True


def delete_current_user(username):
    user = User.objects(username=username)
    user.delete()

    return True