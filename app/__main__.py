from typing import Any

from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute

from app import create_app
import uvicorn

app = create_app()

if __name__ == "__main__":
    uvicorn.run("app:create_app", host="0.0.0.0", port=4567, reload=True, log_level="debug")
