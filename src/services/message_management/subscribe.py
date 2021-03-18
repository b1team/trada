import redis
import time
import json

HOST = 'localhost'
PORT = '6379'
CHANNEL = 'ngocbuidinh'


def subcribe_channel(HOST, PORT, CHANNEL):
    r = redis.Redis(host=HOST, port=PORT)
    pub = r.pubsub()
    pub.subscribe(CHANNEL)

    return pub


def get_message(pub):
    while True:
        data = pub.get_message()
        if data:
            message = data['data']
            if message and message != 1:
                print(json.loads(message))

        time.sleep(0.01)


if __name__ == '__main__':
    pub = subcribe_channel(HOST, PORT, CHANNEL)
    get_message(pub)