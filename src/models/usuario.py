from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioCreate(BaseModel):
    id_rol: int
    id_barrio: int
    id_tipo_documento: int
    doc_usuario: str
    nombre_usuario: str
    apellido_usuario: str
    email_usuario: EmailStr
    telefono_usuario: str
    direccion_usuario: str
    password_usuario: str

class UsuarioResponse(BaseModel):
    id_usuario: int
    id_rol: int
    id_barrio: int
    id_tipo_documento: int
    doc_usuario: str
    nombre_usuario: str
    apellido_usuario: str
    email_usuario: EmailStr
    telefono_usuario: str
    direccion_usuario: str
    estado_rg: Optional[int] = None
    fecha_rg: Optional[datetime] = None
    fecha_md: Optional[datetime] = None

class UsuarioUpdate(BaseModel):
    id_rol: Optional[int] = None
    id_barrio: Optional[int] = None
    id_tipo_documento: Optional[int] = None
    doc_usuario: Optional[str] = None
    nombre_usuario: Optional[str] = None
    apellido_usuario: Optional[str] = None
    email_usuario: Optional[EmailStr] = None
    telefono_usuario: Optional[str] = None
    direccion_usuario: Optional[str] = None
    password_usuario: Optional[str] = None
    estado_rg: Optional[int] = None        

