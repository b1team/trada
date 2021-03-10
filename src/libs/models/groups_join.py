from datetime import datetime
from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    BooleanField
)


class Group_members(Document):
    member_name = StringField(default="")
    group_name = StringField(default="")
    join_at = DateTimeField(default=datetime.utcnow)
    left_at = DateTimeField(default=None)
    left =  BooleanField(default=False)

    def to_dict(self):
        return {
            "group_id": str(self.id),
            "member_name": self.member_name,
            "group_name": self.group_name,
            "join_at": self.join_at,
            "left_at": self.left_at,
            "left": self.left,
        }