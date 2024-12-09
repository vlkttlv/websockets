from fastapi import APIRouter, Depends, Response
from app.exceptions import IncorrectEmailOrPasswordException, UserAlreadyExistsException
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserRegister, SUserLogin
from app.users.dao import UsersDAO
from app.chat.schemas import SMessageCreate, SMessageRead
from app.chat.dao import MessagesDAO
from typing import List

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.get("/messages/{user_id}", summary="Возвращает сообщения между двумя пользователями")
async def get_messages(user_id: int, current_user: Users = Depends(get_current_user)) -> List[SMessageRead]:
    return await MessagesDAO.get_messages_between_users(user_id_1=user_id, user_id_2=current_user.id) or []
    
@router.post("/messages", summary="Отправляет сообщение пользователю")
async def send_message(message: SMessageCreate, current_user: Users = Depends(get_current_user)):
    await MessagesDAO.add(
        sender_id=current_user.id,
        content=message.content,
        recipient_id=message.recipient_id
    )
    
    return {'status': 'successful',
            'recipient_id': message.recipient_id, 
            'content': message.content}