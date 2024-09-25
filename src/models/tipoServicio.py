from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoServicioCreate(BaseModel):
    nombre_tipo_servicio: str

class TipoServicioResponse(BaseModel):
    id_tipo_servicio: int
    nombre_tipo_servicio: str
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class TipoServicioUpdate(BaseModel):
    id_tipo_servicio: int
    nombre_tipo_documento: str
    estado_rg: Optional[int] = None
    fecha_md: Optional[datetime] = None