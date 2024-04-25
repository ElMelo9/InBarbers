from supabase import Client
from src.database.connection import supabase  # Conexión a Supabase
from src.models.login import login,LoginResponse
from pydantic import EmailStr


class LoginRepository:
        
    def __init__(self):
        self.client = supabase

    def getByEmail(self, email_usuario: EmailStr) -> dict:
        response = self.client.from_("usuarios").select("*").eq("email_usuario", email_usuario).execute()
        return response.data[0] if response.data else None       
