from supabase import Client
from src.database.connection import supabase  # Conexión a Supabase
from src.models.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from typing import Optional

class RolesRepository:

    def __init__(self):
        self.client = supabase

    def insert(self, rol_data: dict) -> dict:
        print(rol_data)
        response = self.client.from_("roles").insert(rol_data).execute()
        return response.data[0] if response.data else None

    def getById(self, rol_id: int) -> Optional[dict]:
        response = self.client.from_("roles").select("*").eq("id_rol", rol_id).execute()
        return response.data[0] if response.data else None

    def getAll(self) -> list:
        response = self.client.from_("roles").select("*").execute()
        return response.data

    def update(self, rol_id: int, rol_data: dict) -> Optional[dict]:
        response = self.client.from_("roles").update(rol_data).eq("id_rol", rol_id).execute()
        
        # Devuelve el primer elemento actualizado o None
        return response.data[0] if response.data else None

    def delete(self, rol_id: int) -> bool:
        # Elimina el usuario por ID
        response = self.client.from_("roles").delete().eq("id_rol", rol_id).execute()
        # Devuelve True si la operación fue exitosa, False de lo contrario
        return bool(response.data)