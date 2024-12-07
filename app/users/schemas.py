from pydantic import BaseModel, EmailStr, Field


class SUserRegister(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    firstname: str = Field(..., min_length=3, max_length=50, description="Имя, от 3 до 50 символов")
    lastname: str = Field(..., min_length=3, max_length=50, description="Фамилия, от 3 до 50 символов")
    password: str = Field(..., min_length=8, max_length=50, description="Пароль, от 8 до 50 знаков")
    

class SUserLogin(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=8, max_length=50, description="Пароль, от 8 до 50 знаков")
