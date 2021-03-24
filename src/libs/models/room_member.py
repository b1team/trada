from mongoengine import Document, StringField, BooleanField


class RoomMember(Document):
    room_id = StringField()
    member_id = StringField()
    is_owner = BooleanField(default=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "room_id": self.room_id,
            "member_id": self.member_id
        }