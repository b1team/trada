import datetime

from mongoengine import (DateTimeField, DictField, Document, IntField,
                         ListField, StringField, URLField)


class Groups(Document):
    group_name = StringField(required=True, unique=True)
    group_avatar = URLField(default="https://www.default.com/")
    last_message = DictField(default={})
    unreadCount = IntField(default=0)
    group_members = ListField(DictField(default={}))
    user_created = StringField(default="")
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "group_id": str(self.id),
            "group_name": self.group_name,
            "group_avatar": self.group_avatar,
            "last_message": self.last_message,
            "unreadCount": self.unreadCount,
            "group_members": self.group_members,
            "user_created": self.user_created,
            "created_at": self.created_at,
        }
