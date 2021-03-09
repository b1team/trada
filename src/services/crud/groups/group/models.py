from ...database import db
import datetime


class Groups(db.Document):
    group_id = db.ObjectIdField(db_field="_id")
    group_name = db.StringField(required=True, unique=True)
    group_avatar = db.URLField(default="https://www.default.com/")
    last_message = db.DictField(default={})
    unreadCount = db.IntField(default=0)
    group_members = db.ListField(db.DictField(default={}))
    user_created = db.StringField(default="")
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def to_json(self):
        return {
            "group_id": str(self.group_id),
            "group_name": self.group_name,
            "group_avatar": self.group_avatar,
            "last_message": self.last_message,
            "unreadCount": self.unreadCount,
            "group_members": self.group_members,
            "user_created": self.user_created,
            "created_at": self.created_at,
        }
