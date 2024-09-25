from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServicioCreate(BaseModel):
    id_usuario: int
    id_ubicacion: int
    id_estado_servicio: int
    id_tipo_servicio: int
    precio_servicio: int

class ServicioResponse(BaseModel):
    id_servicio: int
    id_usuario: int
    id_ubicacion: int
    id_estado_servicio: int
    id_tipo_servicio: int
    precio_servicio: int
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class ServicioUpdate(BaseModel):
    id_servicio: int
    id_usuario: int
    id_ubicacion: int
    id_estado_servicio: int
    id_tipo_servicio: int
    precio_servicio: int
    estado_rg: Optional[int] = None
    fecha_md: Optional[datetime] = None