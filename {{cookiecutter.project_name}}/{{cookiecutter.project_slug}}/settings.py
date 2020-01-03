from starlette.config import Config
from starlette.datastructures import Secret, URL

config = Config(".env")
DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URL = config("DATABASE_URL", cast=URL)
REPLICA_DATABASE_URL = config("REPLICA_DATABASE_URL", cast=URL, default="")
ENVIRONMENT = config("PRODUCTION_ENVIRONMENT", default="normal")
SENTRY_DSN = config("SENTRY_DSN")
