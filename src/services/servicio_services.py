from src.models.servicio import ServicioCreate,ServicioResponse,ServicioUpdate
from src.database.repositories.servicio_repo import ServicioRepository

class ServicioService:

    def __init__(self):
        self.servicio_repo = ServicioRepository()

    def insertServicio(self, servicio: ServicioCreate) -> ServicioResponse:

        data_dict = servicio.model_dump()

        response_dict = self.servicio_repo.insert(data_dict)

        return ServicioResponse(**response_dict)


    def getServicioById(self, id: int) -> ServicioResponse:

        response_dict = self.servicio_repo.getById(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return ServicioResponse(**response_dict)
    

    def getServicioByUsuario(self, id: int) -> ServicioResponse:

        response_dict = self.servicio_repo.getByUsuario(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return ServicioResponse(**response_dict)


    def getAllServicio(self) -> list[ServicioResponse]:

        response_dict = self.servicio_repo.getAll()

        servicio_list = [ServicioResponse(**servicio)
                         for servicio in response_dict]

        return servicio_list


    def updateServicio(self, id: int, servicio: ServicioUpdate) -> ServicioResponse:

        data_dict = servicio.model_dump()

        servicio_dict = self.servicio_repo.update(id, data_dict)
        if not servicio_dict:
            raise ValueError("Servicio not found")

        return ServicioResponse(**servicio_dict)


    def deleteServicio(self, id: int):

        return self.servicio_repo.delete(id)

