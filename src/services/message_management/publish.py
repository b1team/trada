import redis
import json


def publish_event(redis_uri, channel, event):
    r = redis.Redis.from_url(redis_uri)
    pub = r.publish(channel=channel, message=json.dumps(event))
    return pub