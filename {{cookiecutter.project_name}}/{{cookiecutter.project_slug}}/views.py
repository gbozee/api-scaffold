import importlib
import typing
import databases
from starlette.applications import Starlette
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.authentication import requires
from starlette.background import BackgroundTasks
from starlette.endpoints import HTTPEndpoint
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.requests import Request
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse, PlainTextResponse, RedirectResponse
from starlette.middleware.cors import CORSMiddleware
import sstarlette
from {{cookiecutter.project_slug}} import settings,utils,service_layer,models



class CustomStarlette(sstarlette.SStarlette):
    def __init__(self, *args, **kwargs):
        super().__init__(
            str(settings.DATABASE_URL),
            replica_database_url=settings.REPLICA_DATABASE_URL,
            serverless=settings.ENVIRONMENT == "serverless",
            model_initializer=models.init_tables,
            **kwargs,
        )
        self.debug = settings.DEBUG
        self.populate_middlewares(
            {% if cookiecutter.auth_backend == 'y' -%}service_layer.verify_access_token,{% endif %}sentry_dsn=settings.SENTRY_DSN
        )

    async def initialize_redis(self):
        self.redis = await utils.redis_connection()
        return self.redis


app = CustomStarlette()

@app.on_event("startup")
async def startup():
    await app.connect_db()

@app.on_event("shutdown")
async def shutdown():
    await app.disconnect_db()

@app.exception_handler(403)
async def not_authorized(request, exc):
    return JSONResponse(
        {"status": False, "msg": "Not Authorized"}, status_code=exc.status_code
    )


@app.route("/")
class Homepage(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse(f"Hello, world!")
