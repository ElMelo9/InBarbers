from src.models.estadoServicio import EstadoServicioCreate, EstadoServicioResponse,EstadoServicioUpdate
from src.services.estado_services import EstadoService
from fastapi import HTTPException

class EstadoController:

    def __init__(self):
        self.estado_service = EstadoService()


    def get_all_estado(self):
        try:
            estados: list[EstadoServicioResponse] = self.estado_service.getAllEstado()

            estados_dicts = [estado.model_dump() for estado in estados]

            return estados_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))
        


    def get_estado_by_id(self,id: int):
        try:
            estado: EstadoServicioResponse= self.estado_service.getEstadoById(id)
            estado= estado.model_dump()

            return estado
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def insert_estado(self, estado:EstadoServicioCreate):
        try:
            estado_response = self.estado_service.insertEstado(estado)
            return (estado_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def update_estado(self,id: int, estado_data:EstadoServicioUpdate):
        try:
            estado: EstadoServicioResponse = self.estado_service.updateEstado(id,estado)
            return (estado.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))     
          

    def delete_estado(self,id: int):
        try:
            return (self.estado_service.deleteEstado(id))
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))       
        