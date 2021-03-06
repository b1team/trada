from ...database import db


class Messages(db.Document):
    message_id = db.ObjectIdField(db_field="_id")
    content = db.StringField()
    senderId = db.ObjectIdField()
    sendername = db.StringField()
    recivedname = db.StringField()
    date = db.StringField(default="5 March")
    timestamp = db.StringField(default="22:00")
    seen = db.BooleanField(default=True)

    def to_json(self):
        return {
            "message_id": str(self.message_id),
            "content": self.content,
            "senderId": str(self.senderId),
            "sendername": self.sendername,
            "recivedname": self.recivedname,
            "date": self.date,
            "timestamp": self.timestamp,
            "seen": self.seen,
        }