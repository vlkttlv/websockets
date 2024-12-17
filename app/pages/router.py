from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.users.dao import UsersDAO
from fastapi import Depends
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/pages", tags=["Фронт"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/auth/register")
async def register(request: Request):
    return templates.TemplateResponse(
        name="register.html", context={"request": request}
    )


@router.get("/auth/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(name="login.html", context={"request": request})


@router.get("/chat/main", response_class=HTMLResponse)
async def chat(request: Request, current_user: Users = Depends(get_current_user)):
    all_users = await UsersDAO.find_all()
    return templates.TemplateResponse(
        name="chat.html",
        context={
            "request": request,
            "all_users": all_users,
            "user": current_user,
        },
    )
