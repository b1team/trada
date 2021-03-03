from .models import User
from src.libs.data_manager import DataManager


def check_user_exist(username: str):
    return False


def save_user(data_manager: DataManager, username, password):
    user = User()
    data_manager.save(user)
    return True