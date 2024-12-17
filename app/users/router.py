from fastapi import APIRouter, Depends, Response
from app.exceptions import IncorrectEmailOrPasswordException, UserAlreadyExistsException
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserRegister, SUserLogin, SUsers
from app.users.dao import UsersDAO
from typing import List

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register", status_code=201)
async def register_user(user_data: SUserRegister):
    """Функция, регистрирующая пользователя"""
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, firstname=user_data.firstname,
                        lastname=user_data.lastname, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    """Функция позволяет пользователю авторизоваться"""
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"access_token": access_token,
            "details": f"привет, {user.firstname} {user.lastname}!"}


@router.post("/logout")
async def logout_user(response: Response):
    """Функция, с помощью которой пользователь выходит из системы. Удаляет действующую куку"""
    response.delete_cookie("access_token")

router_user = APIRouter(
    prefix="/users",
    tags=["Users"]
)
@router_user.get("/")
async def get_users() -> List[SUsers]:
    all_users = await UsersDAO.find_all()
    return all_users