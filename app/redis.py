import aioredis

from app.config.settings import api_settings


def get_redis():
    return aioredis.from_url(api_settings.REDIS_URL,decode_responses=True)

# def set_cache(key,value):
#     redis = get_redis()
#     redis.set(key,value)
#     redis.close()

# def get_cache(key):
#     redis = get_redis()
#     value = redis.get(key)
#     redis.close()
#     return value