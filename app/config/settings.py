import logging
from logging.config import dictConfig
from zoneinfo import ZoneInfo
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    DEBUG: bool = True
    OPENAPI_URL: str | None = "/openapi.json" if DEBUG else None
    API_PREFIX: str = "/api/"
    TIMEZONE_LOCATION: str = "Asia/Seoul"
    ALLOWED_HOSTS: list = []
    CORS_ORIGINS: list = []
    ASYNC_DB_URL: str = "mysql+aiomysql://admin:root@db:3306/admin"

    SWAGGER_UI_PARAMS: dict = {
        "deepLinking": True,
        "defaultModelsExpandDepth": 1,
        "defaultModelExpandDepth": 1,
        "defaultModelRendering": "example",
        "displayRequestDuration": True,
        "docExpansion": "list",
        "filter": True,
        "operationsSorter": "alpha",
        "showExtensions": True,
        "tagsSorter": "alpha",
    }

    SWAGGER_META: dict = {
        "title": "FastAPI",
        "version": "0.1.0",
        "description": "## API by FastAPI",
        "contact": {
            "name": "Hello World",
            "url": "https://github.com",
            "email": "example@gmail.com",
            "license_info": {
                "name": "",
                "url": "",
            },
        },
    }

    LOG_CONFIG: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(levelname)s [%(name)s:%(lineno)s] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "information": {
                "format": "%(levelname)s %(message)s",
            },
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "requests": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }

    @property
    def TIMEZONE(self) -> ZoneInfo:
        return ZoneInfo(self.TIMEZONE_LOCATION)


settings = AppSettings()
dictConfig(settings.LOG_CONFIG)