from ...database import db
import datetime


class Group_members(db.Document):
    member_name = db.StringField(default="")
    group_name = db.StringField(default="")
    join_at = db.DateTimeField(default=datetime.datetime.utcnow)
    left_at = db.DateTimeField(default=None)
    left =  db.BooleanField(default=False)

    def to_json(self):
        return {
            "member_name": self.member_name,
            "group_name": self.group_name,
            "join_at": self.join_at,
            "left_at": self.left_at,
            "left": self.left,
        }