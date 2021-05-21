import datetime

from mongoengine import DateTimeField, Document, StringField, BooleanField


class Admin(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    name = StringField(default="")
    avatar = StringField(
        default="https://cdn2.iconfinder.com/data/icons/zeir-miscellaneous-009/64/admin_user_edit_config-256.png")
    active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "user_id": str(self.id),
            "username": self.username,
            "avatar": self.avatar,
            "name": self.name,
            "active": self.active,
            "created_at": self.created_at,
        }
