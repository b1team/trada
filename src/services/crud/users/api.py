from .logic import (check_user_exist,
                    save_user,
                    update_current_user,
                    delete_current_user,
                    get_user_profile)
# from src.libs.data_manager import MongodbManager


def create_user(username: str, password: str):
    user_exist = check_user_exist(username)
    if not user_exist:
        new_user = save_user(username, password)
        return new_user

    return False


def get_user(username: str):
    user_exist = check_user_exist(username)
    if user_exist:
        user = get_user_profile(username)
        return user

    return False


def update_user(username: str, password: str, avatar: str, name: str):
    user_exist = check_user_exist(username)
    if user_exist:
        user_update = update_current_user(username, password, avatar, name)
        return user_update

    return False


def delete_user(username: str):
    user_exist = check_user_exist(username)
    if user_exist:
        delete_user = delete_current_user(username)
        return delete_user

    return False