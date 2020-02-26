{% if cookiecutter.use_redis|lower == 'y' -%}import aioredis{% endif %}
from {{cookiecutter.project_slug}} import settings

{% if cookiecutter.use_redis|lower == 'y' -%}
async def redis_connection(*args, **kw):
    conn = await aioredis.create_redis(
        settings.CACHE_URL, *args, encoding="utf-8", **kw
    )
    return conn
{% endif %}