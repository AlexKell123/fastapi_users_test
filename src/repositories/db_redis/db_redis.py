import redis


class DBRedis:
    def __init__(self, host='localhost', port=6379, db=0):
        self.type = 'DB_REDIS'
        self.db = redis.Redis(host=host, port=port, db=db)
