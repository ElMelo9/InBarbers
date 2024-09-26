from src.models.estadoServicio import EstadoServicioCreate,EstadoServicioResponse,EstadoServicioUpdate
from src.database.repositories.estado_servicio_repo import EstadoServicioRepository

class EstadoService:

    def __init__(self):
        self.estado_repo = EstadoServicioRepository()

    def insertEstado(self, estado: EstadoServicioCreate) -> EstadoServicioResponse:

        data_dict = estado.model_dump()

        response_dict = self.estado_repo.insert(data_dict)

        return EstadoServicioResponse(**response_dict)


    def getEstadoById(self, id: int) -> EstadoServicioResponse:

        response_dict = self.estado_repo.getById(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("Estado not found")

        return EstadoServicioResponse(**response_dict)


    def getAllEstado(self) -> list[EstadoServicioResponse]:

        response_dict = self.estado_repo.getAll()

        estado_list = [EstadoServicioResponse(**estado)
                         for estado in response_dict]

        return estado_list


    def updateEstado(self, id: int, estado: EstadoServicioUpdate) -> EstadoServicioResponse:

        data_dict = estado.model_dump()

        estado_dict = self.estado_repo.update(id, data_dict)
        if not estado_dict:
            raise ValueError("User not found")

        return EstadoServicioResponse(**estado_dict)


    def deleteEstado(self, id: int):

        return self.estado_repo.delete(id)

