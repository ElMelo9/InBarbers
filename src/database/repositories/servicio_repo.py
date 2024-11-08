from supabase import Client
from src.database.connection import supabase  # Conexión a Supabase
from src.models.asignacion import AsignacionCreate,AsignacionResponse,AsignacionUpdate
from typing import Optional

class ServicioRepository:

    def __init__(self):
        self.client = supabase

    def insert(self, data: dict) -> dict:
        response = self.client.from_("servicios").insert(data).execute()
        return response.data[0] if response.data else None

    def getById(self, id: int) -> Optional[dict]:
        response = self.client.from_("servicios").select("*").eq("id_servicio", id).execute()
        return response.data[0] if response.data else None
    
    def getByUsuario(self, id_usuario: int) -> Optional[dict]:
        response = self.client.from_("servicios").select("*").eq("id_usuario", id_usuario).execute()
        return response.data if response.data else None
    
    def getByTipoServicio(self, id_tipo_servicio: int) -> Optional[dict]:
        response = self.client.from_("servicios").select("*").eq("id_tipo_servicio", id_tipo_servicio).execute()
        return response.data[0] if response.data else None

    def getAll(self) -> list:
        response = self.client.from_("servicios").select("*").execute()
        return response.data

    def update(self, id: int, data: dict) -> Optional[dict]:
        response = self.client.from_("servicios").update(data).eq("id_servicio", id).execute()
        
        # Devuelve el primer elemento actualizado o None
        return response.data[0] if response.data else None

    def delete(self, id: int):
        # Elimina el usuario por ID
        response = self.client.from_("servicios").delete().eq("id_servicio", id).execute()
        # Devuelve True si la operación fue exitosa, False de lo contrario
        return response.data