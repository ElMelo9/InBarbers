from supabase import Client
from src.database.connection import supabase  # Conexión a Supabase
from src.models.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from typing import Optional

class TipoDocRepository:

    def __init__(self):
        self.client = supabase

    def insert(self, tipoDoc_data: dict) -> dict:
        response = self.client.from_("tipo_documento").insert(tipoDoc_data).execute()
        return response.data[0] if response.data else None

    def getById(self, id_tipo_documento: int) -> Optional[dict]:
        response = self.client.from_("tipo_documento").select("*").eq("id_tipo_documento", id_tipo_documento).execute()
        return response.data[0] if response.data else None

    def getAll(self) -> list:
        response = self.client.from_("tipo_documento").select("*").execute()
        return response.data

    def update(self, id_tipo_documento: int, tipoDoc_data: dict) -> Optional[dict]:
        response = self.client.from_("tipo_documento").update(tipoDoc_data).eq("id_tipo_documento", id_tipo_documento).execute()
        
        # Devuelve el primer elemento actualizado o None
        return response.data[0] if response.data else None

    def delete(self, id_tipo_documento: int) -> bool:
        # Elimina el usuario por ID
        response = self.client.from_("tipo_documento").delete().eq("id_tipo_documento",id_tipo_documento).execute()
        # Devuelve True si la operación fue exitosa, False de lo contrario
        return bool(response.data)