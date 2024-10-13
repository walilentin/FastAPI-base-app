from fastapi import APIRouter
from starlette.requests import Request

from core.config import settings, templates

router = APIRouter(prefix=settings.api.v1.pages, tags=["Pages"])


@router.get("")
async def get_auth_page(request: Request):
    return templates.TemplateResponse("start-page.html", {"request": request})


@router.get("/login")
async def get_auth_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})


@router.get("/registration")
async def get_reg_page(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})
