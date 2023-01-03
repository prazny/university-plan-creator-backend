from pathlib import Path
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routes.api import router as api_router
from dotenv import dotenv_values, find_dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv
from app.models.domain.faculty import Faculty
from app.models.domain.field import Field


def get_application() -> FastAPI:
    application = FastAPI()

    config_env = {
        **dotenv_values(),
    }

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix="/api")

    return application

print("aaaaaaas")
app = get_application()
