from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class RolCreate(BaseModel):

    nombre_rol: str

class RolResponse(BaseModel):
    id_rol: int
    nombre_rol: str
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class RolUpdate(BaseModel):
    id_rol: int
    nombre_rol: str
    estado_rg: Optional[int] = None