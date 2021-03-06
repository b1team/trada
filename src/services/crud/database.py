import mongoengine as db
from ...config import settings


db.connect(host=settings.DB_URI)