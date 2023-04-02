import redis
import sys
from datetime import timedelta

def connect_redis() -> redis.client.Redis:
    try:
        client = redis.Redis(host="localhost", port=6379, socket_timeout=5, charset="utf-8", decode_responses=True)
        ping = client.ping()
        if ping is True:
            print("Connected to REDIS")
            return client
    except redis.RedisError:
        print("ERROR connecting to REDIS")
        sys.exit(1)

# The user ID and their corresponding loyalty points are cached.
# The data will retain in cache upto 2 days
def add_to_cache(client, key, value):
    client.setex(key, timedelta(days=2), value=value)

def get_ttl(client, key):
    return client.ttl(key)

def get_from_cache(client, key):
    return client.get(key)

# To be called in main.py file
client = connect_redis()

# TEST: Set userID and their corresponding loyalty point
add_to_cache(client, "user-1234", "30")
print(get_from_cache(client, "user-1334"))