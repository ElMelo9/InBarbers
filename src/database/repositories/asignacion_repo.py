from supabase import Client
from src.database.connection import supabase  # Conexión a Supabase
from src.models.asignacion import AsignacionCreate,AsignacionResponse,AsignacionUpdate
from typing import Optional

class AsignacionRepository:

    def __init__(self):
        self.client = supabase

    def insert(self, asig_data: dict) -> dict:
        response = self.client.from_("asig_servicio").insert(asig_data).execute()
        return response.data[0] if response.data else None

    def getById(self, id_asig: int) -> Optional[dict]:
        response = self.client.from_("asig_servicio").select("*").eq("id_asig", id_asig).execute()
        return response.data[0] if response.data else None
    
    def getByUsuario(self, id_usuario: str) -> Optional[dict]:
        response = self.client.from_("asig_servicio").select("*").eq("id_usuario", id_usuario).execute()
        return response.data[0] if response.data else None
    
    def getByServicio(self, id_servicio: int) -> Optional[dict]:
        response = self.client.from_("asig_servicio").select("*").eq("id_servicio", id_servicio).execute()
        return response.data[0] if response.data else None

    def getAll(self) -> list:
        response = self.client.from_("asig_servicio").select("*").execute()
        return response.data

    def update(self, id_asig: int, asig_data: dict) -> Optional[dict]:
        response = self.client.from_("asig_servicio").update(asig_data).eq("id_asig", id_asig).execute()
        
        # Devuelve el primer elemento actualizado o None
        return response.data[0] if response.data else None

    def delete(self, id_asig: int):
        # Elimina el usuario por ID
        response = self.client.from_("asig_servicio").delete().eq("id_asig", id_asig).execute()
        # Devuelve True si la operación fue exitosa, False de lo contrario
        return response.data
