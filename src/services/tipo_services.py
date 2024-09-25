from src.models.tipoServicio import TipoServicioCreate, TipoServicioResponse, TipoServicioUpdate
from src.database.repositories.tipo_servicio_repo import TipoServicioRepository

class TipoService:

    def __init__(self):
        self.tipo_repo = TipoServicioRepository()

    def insertTipoServicio(self, tipo: TipoServicioCreate) -> TipoServicioResponse:

        data_dict = tipo.model_dump()

        response_dict = self.tipo_repo.insert(data_dict)

        return TipoServicioResponse(**response_dict)


    def getTipoServicioById(self, id: int) -> TipoServicioResponse:

        response_dict = self.tipo_repo.getById(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return TipoServicioResponse(**response_dict)
    

    def getAllTipoServicio(self) -> list[TipoServicioResponse]:

        response_dict = self.tipo_repo.getAll()

        tipo_list = [TipoServicioResponse(**tipo)
                         for tipo in response_dict]

        return tipo_list


    def updateTipoServicio(self, id: int, tipo: TipoServicioUpdate) -> TipoServicioResponse:

        data_dict = tipo.model_dump()

        servicio_dict = self.tipo_repo.update(id, data_dict)
        if not servicio_dict:
            raise ValueError("Servicio not found")

        return TipoServicioResponse(**servicio_dict)


    def deleteTipoServicio(self, id: int):

        return self.tipo_repo.delete(id)

