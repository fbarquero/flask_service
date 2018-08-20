import redis


class RedisConn:

    def __init__(self):
        self._r = redis.Redis(
            host='redis',
            port=6379)

    def redis_write(self, key, value):
        try:
            r = self._r.set(key, value)
            return r
        except Exception as e:
            print(e.message)
            return None

    def redis_read(self, key):
        try:
            rs = self._r.get(key)
            return rs
        except Exception as e:
            print(e.message)
            return None
