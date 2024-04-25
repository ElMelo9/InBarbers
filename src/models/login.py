from pydantic import BaseModel, EmailStr



class Login(BaseModel):
    email_usuario: EmailStr
    password_usuario: str


class LoginResponse(BaseModel):
    
    token_usuario: str
    token_tipo: str
