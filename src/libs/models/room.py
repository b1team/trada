from mongoengine import StringField, Document


class Room(Document):
    type = StringField(default="private")
    room_name = StringField(required=True)
    display_name = StringField(default="")

    def to_dict(self):
        return {
            "id": str(self.id),
            "type": self.type,
            "room_name": self.room_name,
            "display_name": self.display_name,
        }