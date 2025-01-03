from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.responses import RedirectResponse

from api import router as api_router
from core.config import settings
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield
    # shutdown
    print("Dispose engine")
    await db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

main_app.include_router(
    api_router,
)


@main_app.get("/")
async def redirect_to_auth():
    return RedirectResponse(url="/api/v1/pages")


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )