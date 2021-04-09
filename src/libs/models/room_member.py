from mongoengine import Document, StringField, BooleanField, DateTimeField
from datetime import datetime


class RoomMember(Document):
    room_id = StringField()
    member_id = StringField()
    is_owner = BooleanField(default=False)
    join_date = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.id),
            "room_id": self.room_id,
            "member_id": self.member_id,
            "join_date": self.join_date
        }