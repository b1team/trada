from mongoengine import(
    Document,
    StringField,
    BooleanField
)
from datetime import datetime

from mongoengine.fields import DateTimeField


class Messages(Document):
    content = StringField()
    sender_id = StringField()
    receiver_id = StringField()
    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())
    seen = BooleanField(default=False)

    def to_dict(self):
        return {
            "message_id": str(self.id),
            "content": self.content,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "seen": self.seen,
        }