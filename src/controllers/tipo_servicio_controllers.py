from src.models.tipoServicio import TipoServicioCreate, TipoServicioResponse, TipoServicioUpdate
from src.services.tipo_services import TipoService
from fastapi import HTTPException

class TipoServicioController:

    def __init__(self):
        self.Tiposervice = TipoService()


    def get_all_TipoServicio(self):
        try:
            tipos: list[TipoServicioResponse] = self.Tiposervice.getAllTipoServicio()

            tipos_dicts = [tipo.model_dump() for tipo in tipos]

            return tipos_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))
        


    def get_TipoServicio_by_id(self,id: int):
        try:
            TipoServicio: TipoServicioResponse= self.Tiposervice.getTipoServicioById(id)
            TipoServicio= TipoServicio.model_dump()

            return TipoServicio
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def insert_TipoServicio(self, TipoServicio:TipoServicioCreate):
        try:
            TipoServicio_response = self.Tiposervice.insertTipoServicio(TipoServicio)
            return (TipoServicio_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def update_TipoServicio(self,id: int, TipoServicio_data:TipoServicioUpdate):
        try:
            TipoServicio: TipoServicioResponse = self.Tiposervice.updateTipoServicio(id,TipoServicio)
            return (TipoServicio.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))     
          

    def delete_TipoServicio(self,id: int):
        try:
            return (self.Tiposervice.deleteTipoServicio(id))
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))       
        