import os
from  redis import from_url
from rq import Worker, Queue, Connection

listen = ['latteq']
region = os.environ.get("REGION")
redis_url = f"redis://redis-{region}:6379/1"
conn = from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        print("Test", flush=True)
        worker = Worker(list(map(Queue, listen)))
        worker.work()