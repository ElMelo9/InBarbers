from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BarrioCreate(BaseModel):

    nombre_barrio: str

class BarrioResponse(BaseModel):
    id_barrio: int
    nombre_barrio: str
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class BarrioUpdate(BaseModel):
    id_barrio: str
    nombre_barrio: str
    estado_rg: Optional[int] = None