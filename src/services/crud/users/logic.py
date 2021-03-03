from .models import User


def check_user_exist(username: str):
    return False


def save_user(username, password):
    user = User()
    print("Saved user to database")
    return True