from src.models.ubicacion import UbicacionCreate,UbicacionResponse,UbicacionUpdate
from src.database.repositories.ubicacion_repo import UbicacionRepository

class UbicacionService:

    def __init__(self):
        self.tipo_repo = UbicacionRepository()

    def insertubicacion(self, ubicacion: UbicacionCreate) -> UbicacionResponse:

        data_dict = ubicacion.model_dump()

        response_dict = self.tipo_repo.insert(data_dict)

        return UbicacionResponse(**response_dict)


    def getUbicacionById(self, id: int) -> UbicacionResponse:

        response_dict = self.tipo_repo.getById(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return UbicacionResponse(**response_dict)
    

    def getUbicacionByUsuario(self, id: int) -> UbicacionResponse:

        response_dict = self.tipo_repo.getByUsuario(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return UbicacionResponse(**response_dict)
    

    def getAllUbicacion(self) -> list[UbicacionResponse]:

        response_dict = self.tipo_repo.getAll()

        ubicacion_list = [UbicacionResponse(**ubicacion)
                         for ubicacion in response_dict]

        return ubicacion_list


    def updateUbicacion(self, id: int, ubicacion: UbicacionUpdate) -> UbicacionResponse:

        data_dict = ubicacion.model_dump()

        ubicacion_dict = self.tipo_repo.update(id, data_dict)
        if not ubicacion_dict:
            raise ValueError("Ubicacion not found")

        return UbicacionResponse(**ubicacion_dict)


    def deleteTipoServicio(self, id: int):

        return self.tipo_repo.delete(id)
