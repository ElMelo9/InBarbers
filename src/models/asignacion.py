from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AsignacionCreate(BaseModel):
    id_servicio: int
    id_usuario: int

class AsignacionResponse(BaseModel):
    id_asig: int
    id_servicio: int
    id_usuario: int
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class AsignacionUpdate(BaseModel):
    id_asig: int
    id_servicio: int
    id_usuario: int
    estado_rg: Optional[int] = None
    fecha_md: Optional[datetime] = None