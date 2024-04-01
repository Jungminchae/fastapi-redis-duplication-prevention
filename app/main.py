import logging
from fastapi import FastAPI
from fastapi_mctools.middlewares.logging import RequestLoggingMiddleware
from app.routes.routers import router

logger = logging.getLogger("requests")


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    app.add_middleware(RequestLoggingMiddleware, logger=logger)
    return app


app = create_app()