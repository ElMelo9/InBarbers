from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EstadoServicioCreate(BaseModel):
    nombre_estado_servicio: str

class EstadoServicioResponse(BaseModel):
    id_estado_servicio: int
    nombre_estado_servicio: str
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class EstadoServicioUpdate(BaseModel):
    id_estado_servicio: int
    nombre_estado_servicio: str
    estado_rg: Optional[int] = None
    fecha_md: Optional[datetime] = None