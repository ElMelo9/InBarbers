from src.models.ubicacion import UbicacionCreate,UbicacionResponse,UbicacionUpdate
from src.services.ubicacion_services import UbicacionService
from fastapi import HTTPException

class TipoServicioController:

    def __init__(self):
        self.ubicacionService =  UbicacionService()


    def get_all_ubicacion(self):
        try:
            ubicaciones: list[UbicacionResponse] = self.ubicacionService.getAllUbicacion()

            ubicaciones_dicts = [ubicacion.model_dump() for ubicacion in ubicaciones]

            return ubicaciones_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))
        


    def get_ubicacion_by_id(self,id: int):
        try:
            ubicacion: UbicacionResponse= self.ubicacionService.getUbicacionById(id)
            ubicacion= ubicacion.model_dump()

            return ubicacion
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def insert_ubicacion(self, ubicacion:UbicacionCreate):
        try:
            ubicacion_response = self.ubicacionService.insertubicacion(ubicacion)
            return (ubicacion_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def update_ubicacion(self,id: int, ubicacion_data:UbicacionUpdate):
        try:
            ubicacion: UbicacionResponse = self.ubicacionService.updateUbicacion(id,ubicacion)
            return (ubicacion.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))     
          

    def delete_ubicacion(self,id: int):
        try:
            return (self.ubicacionService.deleteUbicacion(id))
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))       
        