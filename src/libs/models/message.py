from mongoengine import(
    Document,
    StringField,
    BooleanField
)


class Messages(Document):
    content = StringField()
    senderId = StringField()
    sendername = StringField()
    recivedname = StringField()
    date = StringField(default="5 March")
    timestamp = StringField(default="22:00")
    seen = BooleanField(default=True)

    def to_dict(self):
        return {
            "message_id": str(self.id),
            "content": self.content,
            "senderId": self.senderId,
            "sendername": self.sendername,
            "recivedname": self.recivedname,
            "date": self.date,
            "timestamp": self.timestamp,
            "seen": self.seen,
        }