import importlib
import typing

from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import (JSONResponse, PlainTextResponse )

from sstarlette{% if cookiecutter.sql_database|lower == 'y' -%}.sql{% elif cookiecutter.auth_backend|lower == 'y' -%}.with_middleware{% else %}{% endif %} import SStarlette
from {{cookiecutter.project_slug}} import ({% if cookiecutter.sql_database|lower == 'y' -%}models,{% endif %} service_layer, settings,)

async def not_authorized(request, exc):
    return JSONResponse(
        {"status": False, "msg": "Not Authorized"}, status_code=exc.status_code
    )

class Homepage(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse(f"Hello, world!")
config = {
    "service_layer": service_layer.service,
    "routes":[Route("/",HomePage,methods=['GET'])],
    "debug": settings.DEBUG,
    "exception_handlers": {403:not_authorized},
    "serverless":settings.ENVIRONMENT == "serverless",
{% if cookiecutter.sql_database|lower == 'y' -%}
    "database_url":str(settings.DATABASE_URL),
    "model_initializer":models.init_tables,
    "replica_database_url":settings.REPLICA_DATABASE_URL,
{% endif %}
{% if cookiecutter.auth_backend|lower == 'y' -%}
    "auth_token_verify_user_callback":service_layer.verify_access_token,
    "auth_result_callback":service_layer.auth_result_callback.
{% endif %}
{% if cookiecutter.sentry_support|lower == 'y' -%}
    "sentry_dsn":settings.SENTRY_DSN.
{% endif %}
}
app = SStarlete(**config)




