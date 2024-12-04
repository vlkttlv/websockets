from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    name: str
    password: str

