import redis
from rq import Worker, Queue, Connection
from configs import REDIS_URL


redis_conn = redis.from_url(REDIS_URL)
listen = ['high', 'default', 'low']


if __name__ == '__main__':
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work(with_scheduler=True)
