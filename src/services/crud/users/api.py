from .logic import check_user_exist, save_user


def create_user(username: str, password: str):
    user_exist = check_user_exist(username)
    if not user_exist:
        user_id = save_user(username, password)
        return user_id
    return None