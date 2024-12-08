from fastapi import APIRouter, Depends, Response
from app.exceptions import IncorrectEmailOrPasswordException, UserAlreadyExistsException
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserRegister, SUserLogin
from app.users.dao import UsersDAO

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)
