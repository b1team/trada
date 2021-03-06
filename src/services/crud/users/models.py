from ..database import db
import datetime


class User(db.Document):
    user_id = db.ObjectIdField(db_field='_id')
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    name = db.StringField(default="")
    avatar = db.URLField(default="https://www.default.com/")
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def to_json(self):
        return {
                "user_id" : str(self.user_id),
                "username" : self.username,
                "avatar" : self.avatar,
                "password" : self.password,
                "name" : self.name,
                "created_at" : self.created_at
                }
