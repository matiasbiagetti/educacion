from fastapi import Depends
from pydantic import BaseModel

from app.models.clase import Clase
from app.repository.clases_repository import ClasesRepository


class ClaseData(BaseModel):
    nombre: str
    descripcion: str
    id_curso: int


class ClasesService:
    """
    Clases Service
    """

    def __init__(self, clases_respository: ClasesRepository = Depends(ClasesRepository)) -> None:
        self.clases_repository = clases_respository

    def crear_clase(self, clase_data: ClaseData) -> Clase:
        """
        Crea una clase
        """
        colegio = self.colegios_service.get_by_curso_id(clase_data.id_curso)
        clase = Clase(nombre=clase_data.nombre, descripcion=clase_data.descripcion, curso_id=clase_data.id_curso,
                      colegio_id=colegio.id)
        return self.clases_repository.crear_clase(clase)

    def get_all(self) -> list:
        """
        Devuelve todas las clases
        """
        return self.clases_repository.get_all()

    def get_by_id(self, codigo: int) -> Clase:
        """
        Devuelve una clase por su id
        """
        return self.clases_repository.get_by_codigo(codigo)

    def get_by_curso_id(self, curso_id: int) -> list:
        """
        Devuelve todas las clases de un curso
        """
        return self.clases_repository.get_by_curso_id(curso_id)
