from src.models.asignacion import AsignacionCreate,AsignacionResponse,AsignacionUpdate
from src.database.repositories.asignacion_repo import AsignacionRepository

class AsignacionService:

    def __init__(self):
        self.asig_repo = AsignacionRepository()

    def insertAsignacion(self, asign: AsignacionCreate) -> AsignacionResponse:

        data_dict = asign.model_dump()

        response_dict = self.asig_repo.insert(data_dict)

        return AsignacionResponse(**response_dict)


    def getAsingnacionById(self, id: int) -> AsignacionResponse:

        response_dict = self.asig_repo.getById(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return AsignacionResponse(**response_dict)

    def getAsingnacionByUsuario(self, id: int) -> AsignacionResponse:

        response_dict = self.asig_repo.getByUsuario(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return AsignacionResponse(**response_dict)
    

    def getAsingnacionByServicio(self, id: int) -> AsignacionResponse:

        response_dict = self.asig_repo.getByServicio(id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return AsignacionResponse(**response_dict)


    def getAllAsignacion(self) -> list[AsignacionResponse]:

        response_dict = self.asig_repo.getAll()

        asing_list = [AsignacionResponse(**asignacion)
                         for asignacion in response_dict]

        return asing_list


    def updateAsignacion(self, id: int, asignacion: AsignacionUpdate) -> AsignacionResponse:

        data_dict = asignacion.model_dump()

        asign_dict = self.asig_repo.update(id, data_dict)
        if not asign_dict:
            raise ValueError("User not found")

        return AsignacionResponse(**asign_dict)


    def deleteAsignacion(self, id: int):

        return self.asig_repo.delete(id)

