from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoDocCreate(BaseModel):
    nombre_tipo_documento: str
    sigla_tipo_documento: str

class TipoDocResponse(BaseModel):
    id_tipo_documento: int
    nombre_tipo_documento: str
    sigla_tipo_documento: str
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class TipoDocUpdate(BaseModel):
    nombre_tipo_documento: str
    sigla_tipo_documento: str
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None  