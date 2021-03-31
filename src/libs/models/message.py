from datetime import datetime

from mongoengine import BooleanField, Document, StringField, DateTimeField


class Messages(Document):
    content = StringField()
    sender_id = StringField()
    room_id = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    seen = BooleanField(default=False)
    active = BooleanField(default=True)

    def to_dict(self):
        return {
            "message_id": str(self.id),
            "content": self.content,
            "sender_id": self.sender_id,
            "room_id": self.room_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "seen": self.seen,
            "active": self.active,
        }
