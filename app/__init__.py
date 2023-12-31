from typing import Any

from fastapi import FastAPI, APIRouter
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware

from app.configs.sqlalchemy import mapper_registry_configure
from app.routers.colegios_router import colegios_router
from app.routers.cursos_router import cursos_router
from app.routers.estudiantes_router import estudiantes_router
from app.routers.feedback_router import feedback_router
from app.routers.ping_router import ping_router
from app.routers.propuestas_router import propuestas_router


def create_app() -> FastAPI:
    app = FastAPI(
        swagger_ui_parameters={

        }
    )

    mapper_registry_configure()

    def custom_openapi() -> Any:
        """
        Customize openapi function
        """
        if not app.openapi_schema:
            routes = []
            for route in app.routes:
                if isinstance(route, APIRouter):
                    routes.extend(route.routes)
                else:
                    routes.append(route)

            app.openapi_schema = get_openapi(
                title="TeachTrack API",
                version="0.1.0",
                openapi_version="3.0.2",
                description="API para el proyecto de TeachTrack",
                routes=routes,
            )
        return app.openapi_schema

    app.openapi = custom_openapi
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(colegios_router)
    app.include_router(cursos_router)
    app.include_router(estudiantes_router)
    app.include_router(feedback_router)
    app.include_router(ping_router)
    app.include_router(propuestas_router)

    return app
