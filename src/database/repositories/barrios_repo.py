from supabase import Client
from src.database.connection import supabase  # Conexión a Supabase
from src.models.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from typing import Optional

class BarriosRepository:

    def __init__(self):
        self.client = supabase

    def insert(self, barrio_data: dict) -> dict:
        response = self.client.from_("barrios").insert(barrio_data).execute()
        return response.data[0] if response.data else None

    def getById(self, id_barrio: int) -> Optional[dict]:
        response = self.client.from_("barrios").select("*").eq("id_barrio", id_barrio).execute()
        return response.data[0] if response.data else None

    def getAll(self) -> list:
        response = self.client.from_("barrios").select("*").execute()
        return response.data

    def update(self, id_barrio: int, barrio_data: dict) -> Optional[dict]:
        response = self.client.from_("barrios").update(barrio_data).eq("id_barrio", id_barrio).execute()
        
        # Devuelve el primer elemento actualizado o None
        return response.data[0] if response.data else None

    def delete(self, id_barrio: int) -> bool:
        # Elimina el usuario por ID
        response = self.client.from_("barrios").delete().eq("id_barrio",id_barrio).execute()
        # Devuelve True si la operación fue exitosa, False de lo contrario
        return bool(response.data)