from starlette.config import Config
from starlette.datastructures import Secret, URL

config = Config(".env")
DEBUG = config("DEBUG", cast=bool, default=False)
{% if cookiecutter.sql_database|lower == 'y' -%}
DATABASE_URL = config("DATABASE_URL", cast=URL)
REPLICA_DATABASE_URL = config("REPLICA_DATABASE_URL", cast=URL, default="")
{% endif %}
ENVIRONMENT = config("PRODUCTION_ENVIRONMENT", default="normal")

{% if cookiecutter.sentry_support|lower == 'y' -%}
SENTRY_DSN = config("SENTRY_DSN")
{% endif %}
