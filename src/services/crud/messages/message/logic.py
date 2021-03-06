from .models import Messages
from bson import ObjectId


def save_messages(content, senderId, sendername, recivedname, date, timestamp):
    message = Messages.objects(content=content,
                               senderId=senderId,
                               sendername=sendername,
                               recivedname=recivedname,
                               date=date,
                               timestamp=timestamp)
    message.save()

    return True


def get_messages(sendername, recivedname):
    messages = Messages.objects(sendername=sendername, recivedname=recivedname)
    list_messages = []
    for message in messages:
        list_messages.append(message)

    return list_messages


def update_messages(message_id, content):
    message = Messages.objects(message_id=ObjectId(message_id))
    filed = {
        "content": content,
    }

    message.update(**filed)
    message.reload()

    return True


def delete_messages(sendername, recivedname, content):
    messages = Messages.objects(sendername=sendername,
                                recivedname=recivedname,
                                content=content)
    messages.delete()

    return True