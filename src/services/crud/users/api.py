from .logic import check_user_exist, save_user
from src.libs.data_manager import MongodbManager


def create_user(username: str, password: str):
    user_exist = check_user_exist(username)
    if not user_exist:
        mongo_manager = MongodbManager()
        user_id = save_user(mongo_manager, username, password)
        return user_id
    return None