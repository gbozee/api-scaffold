import importlib
import typing

import databases
from starlette.applications import Starlette
from starlette.authentication import requires
from starlette.background import BackgroundTasks
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import (JSONResponse, PlainTextResponse,
                                 RedirectResponse)

import sstarlette
from {{cookiecutter.project_slug}} import (models, service_layer, settings,
                                           utils)

async def not_authorized(request, exc):
    return JSONResponse(
        {"status": False, "msg": "Not Authorized"}, status_code=exc.status_code
    )

class CustomStarlette(sstarlette.SStarlette):
    def __init__(self, *args, **kwargs):
        middlewares = self.populate_middlewares(
            {% if cookiecutter.auth_backend == 'y' -%}service_layer.verify_access_token,{% endif %}sentry_dsn=settings.SENTRY_DSN,
            debug=settings.DEBUG,
        )
        super().__init__(
            str(settings.DATABASE_URL),
            middleware=middlewares,
            debug=settings.DEBUG,
            replica_database_url=settings.REPLICA_DATABASE_URL,
            serverless=settings.ENVIRONMENT == "serverless",
            model_initializer=models.init_tables,
            exception_handlers={403: not_authorized},
            **kwargs,
        )

    async def initialize_redis(self):
        self.redis = await utils.redis_connection()
        return self.redis

class Homepage(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse(f"Hello, world!")

app = CustomStarlette(service_layer=service_layer.service, routes=[Route("/",HomePage,methods=['GET'])])




