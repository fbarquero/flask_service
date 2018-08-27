from redis_connector import RedisConn


class RedisActions:

    def __init__(self):
        self.conn = RedisConn()

    def redis_write(self, key, value):
        k = self.conn.redis_write(key, value)
        return k

    def redis_read(self, key):
        k = self.conn.redis_read(key)
        return k