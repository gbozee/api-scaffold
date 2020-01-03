import aioredis
from {{cookiecutter.project_slug}} import settings

async def redis_connection(*args, **kw):
    conn = await aioredis.create_redis(
        settings.CACHE_URL, *args, encoding="utf-8", **kw
    )
    return conn
