from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UbicacionCreate(BaseModel):
    id_usuario: int
    longitud_usuario: str
    latitud_usuario: str

class UbicacionResponse(BaseModel):
    id_ubicacion: int
    id_usuario: int
    longitud_usuario: str
    latitud_usuario: str
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class UbicacionUpdate(BaseModel):
    id_ubicacion: int
    id_usuario: int
    longitud_usuario: str
    latitud_usuario: str
    estado_rg: Optional[int] = None
    fecha_md: Optional[datetime] = None