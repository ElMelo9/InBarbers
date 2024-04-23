from supabase import Client
from src.database.connection import supabase  # Conexión a Supabase
from src.models.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from typing import Optional

class UsuariosRepository:

    def __init__(self):
        self.client = supabase

    def insert(self, user_data: dict) -> dict:
        response = self.client.from_("usuarios").insert(user_data).execute()
        return response.data[0] if response.data else None

    def getById(self, user_id: int) -> Optional[dict]:
        response = self.client.from_("usuarios").select("*").eq("id_usuario", user_id).execute()
        return response.data[0] if response.data else None

    def getAll(self) -> list:
        response = self.client.from_("usuarios").select("*").execute()
        return response.data

    def update(self, user_id: int, user_data: dict) -> Optional[dict]:
        response = self.client.from_("usuarios").update(user_data).eq("id_usuario", user_id).execute()
        
        # Devuelve el primer elemento actualizado o None
        return response.data[0] if response.data else None

    def delete(self, user_id: int) -> bool:
        # Elimina el usuario por ID
        response = self.client.from_("usuarios").delete().eq("id_usuario", user_id).execute()
        # Devuelve True si la operación fue exitosa, False de lo contrario
        return bool(response.data)
