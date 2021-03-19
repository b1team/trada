from .models import Groups


def check_group_exists(group_name):
    group = Groups.objects(group_name=group_name).first()
    if group:
        return True

    return False


def save_group(group_name, user):
    group = Groups(group_name=group_name, user_created=user)
    group.save()

    return True


def get_group_profile(group_name):
    group = Groups.objects(group_name=group_name).first()

    return group.to_json()


def update_group_profile(group_name, group_avatar):
    group = Groups.objects(group_name=group_name)
    fileds = {
        "group_name": group_name,
        "group_avatar": group_avatar,
    }
    group.update(**fileds)
    group.reload()

    return True


def destroy_group(group_name):
    group = Groups.objects(group_name=group_name)
    group.delete()

    return True