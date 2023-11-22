# import aioredis
import redis


from app.config.settings import api_settings

def get_redis():
    return redis.from_url(api_settings.REDIS_URL,decode_responses=True)


