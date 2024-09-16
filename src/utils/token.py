from dotenv import load_dotenv
from datetime import datetime, timedelta
from src.models.usuario import UsuarioResponse
from src.models.login import LoginResponse
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
import os
import jwt
import pytz

# Ruta para obtener el token (usada por OAuth2PasswordBearer)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

class Token:
     
     def __init__(self):

        load_dotenv()
        self.token_expire = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        self.token_algorithm = os.getenv("ALGORITHM")
        self.token_key = os.getenv("SECRET_KEY")
        self.tz = pytz.timezone('America/Bogota')

     def generarToken(self,usuario: UsuarioResponse)-> dict:
        expiration = datetime.now(tz=self.tz) + timedelta(minutes=self.token_expire)
        payload = {
                'exp': expiration,
                'id_usuario': usuario['id_usuario'],
                'Nombre_usuario': usuario['nombre_usuario'] + ' ' + usuario['apellido_usuario'],
                'rol': usuario['id_rol'],
                'email':usuario['email_usuario']

                }
        # Generar el token JWT
        token_usuario = jwt.encode(payload, self.token_key, algorithm=self.token_algorithm)

        return {
            "token_usuario": token_usuario,
            "token_tipo": "bearer"
        }
     

     def decodificarToken(self,token: str):
        try:
            # Decodificar el token
            payload = jwt.decode(
                token,
                self.token_key,
                algorithms=[self.token_algorithm]
            )
            return payload  # Retorna el payload decodificado
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )



# Función para obtener el usuario actual a partir del token
def verificarToken(token: str = Depends(oauth2_scheme)):
    token_instance = Token()
    try:
        return token_instance.decodificarToken(token)
    except HTTPException as he:
        raise he