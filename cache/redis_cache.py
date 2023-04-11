import redis
import sys
from datetime import timedelta

class RedisClient():
    
    def __init__(self):
        try:
            self.client = redis.Redis(host="redis", port=6379, socket_timeout=5, charset="utf-8", decode_responses=True)
            ping = self.client.ping()
            if ping is True:
                print("Connected to REDIS")
        except redis.RedisError:
            print("ERROR connecting to REDIS")
            sys.exit(1)

    # The user ID and their corresponding loyalty points are cached.
    # The data will retain in cache upto 2 days
    def add_to_cache(self, key, value):
        self.client.setex(key, timedelta(days=1), value=value)

    def get_ttl(self, key):
        return self.client.ttl(key)

    def get_from_cache(self, key):
        return self.client.get(key)

    def get_redis_client(self):
        return self.client

    # TEST: Set userID and their corresponding loyalty point
    # add_to_cache(client, "user-1234", "30")
    # print(get_from_cache(client, "user-1334"))