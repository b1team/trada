from mongoengine import StringField, Document, DateTimeField
from datetime import datetime


class Room(Document):
    type = StringField(default="private")
    room_name = StringField(required=True)
    display_name = StringField(default="")
    avatar = StringField(default="")
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.id),
            "type": self.type,
            "room_name": self.room_name,
            "display_name": self.display_name,
            "avatar": self.avatar,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }