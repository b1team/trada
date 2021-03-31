import datetime

from mongoengine import DateTimeField, Document, StringField, BooleanField


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    name = StringField(default="")
    avatar = StringField(
        default="https://image.flaticon.com/icons/png/128/860/860784.png")
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
