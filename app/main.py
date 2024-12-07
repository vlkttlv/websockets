from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.users.router import router as users_router
# from app.chat.router import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
from app.pages.router import router as pages_router
app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), name='static')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с любых источников. Можете ограничить список доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

app.include_router(users_router)
app.include_router(pages_router)