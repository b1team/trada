from src.libs.models.groups import Groups

from typing import Optional

from bson import ObjectId



def check_group_exists(group_id):
    group = Groups.objects(id=ObjectId(group_id)).first()
    if group:
        return True

    return False


def get_group(group_name: str):
    return Groups.objects(group_name=group_name).first()


def save_group(
    group_name: str,
    username:str
):
    group = Groups(group_name=group_name, user_created=username)

    return group.save()



def get_group_profile(group_name):
    group = Groups.objects(group_name=group_name).first()

    return group.to_json()


def update_group_profile(
    group_name: str,
    group_avatar: Optional[str] = None
):
    group = Groups.objects(group_name=group_name)
    fileds = {
        "group_avatar": group_avatar,
    }
    group.update(**fileds)

    return True


def delete_group(group_name):
    group = Groups.objects(group_name=group_name)
    group.delete()

    return True