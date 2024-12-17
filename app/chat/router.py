from fastapi import APIRouter, Depends, Response, WebSocket
from app.exceptions import IncorrectEmailOrPasswordException, UserAlreadyExistsException
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.chat.schemas import SMessageCreate, SMessageRead
from app.users.schemas import SUserRegister, SUserLogin
from app.chat.dao import MessagesDAO
from app.users.dao import UsersDAO
from typing import List, Dict

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

    # Подготавливаем данные для отправки сообщения
    message_data = {
        'sender_id': current_user.id,
        'recipient_id': message.recipient_id,
        'content': message.content,
    }
    
    # Уведомляем получателя и отправителя через WebSocket
    await notify_user(message.recipient_id, message_data)
    await notify_user(current_user.id, message_data)


    return {'status': 'successful',
            'recipient_id': message.recipient_id, 
            'content': message.content}

# Активные WebSocket-подключения: {user_id: websocket}
active_connections: Dict[int, WebSocket] = {}


async def notify_user(user_id: int, message: dict):
    """Функция для отправки сообщения пользователю, если он подключен"""
    if user_id in active_connections:
        websocket = active_connections[user_id]
        await websocket.send_json(message) # Отправляем сообщение в формате JSON

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()  # Принимаем WebSocket-соединение
    active_connections[user_id] = websocket # Сохраняем активное соединение для пользователя
    try:
        while True:
            await asyncio.sleep(1) # Просто поддерживаем соединение активным (1 секунда паузы)
    except WebSocketDisconnect:
        active_connections.pop(user_id, None) # Удаляем пользователя из активных соединений при отключении