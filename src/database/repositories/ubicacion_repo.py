from supabase import Client
from src.database.connection import supabase  # Conexión a Supabase
from src.models.asignacion import AsignacionCreate,AsignacionResponse,AsignacionUpdate
from typing import Optional

class UbicacionRepository:

    def __init__(self):
        self.client = supabase

    def insert(self, data: dict) -> dict:
        response = self.client.from_("ubicaciones").insert(data).execute()
        return response.data[0] if response.data else None

    def getById(self, id: int) -> Optional[dict]:
        response = self.client.from_("ubicaciones").select("*").eq("id_ubicacion", id).execute()
        return response.data[0] if response.data else None
    
    def getByUsuario(self, id: int) -> Optional[dict]:
        response = self.client.from_("ubicaciones").select("*").eq("id_usuario", id).execute()
        return response.data[0] if response.data else None
    

    def getAll(self) -> list:
        response = self.client.from_("ubicaciones").select("*").execute()
        return response.data

    def update(self, id: int, data: dict) -> Optional[dict]:
        response = self.client.from_("ubicaciones").update(data).eq("id_ubicacion", id).execute()
        
        # Devuelve el primer elemento actualizado o None
        return response.data[0] if response.data else None

    def delete(self, id: int):
        # Elimina el usuario por ID
        response = self.client.from_("ubicaciones").delete().eq("id_ubicacion", id).execute()
        # Devuelve True si la operación fue exitosa, False de lo contrario
        return response.data