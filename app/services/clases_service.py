from fastapi import Depends
from pydantic import BaseModel

from app.models.clase import Clase
from app.repository.clases_repository import ClasesRepository
from app.services.colegios_service import ColegiosService


class ClaseData(BaseModel):
    nombre: str
    descripcion: str
    curso_codigo: int


class ClasesService:
    """
    Clases Service
    """

    def __init__(self, clases_respository: ClasesRepository = Depends(ClasesRepository),
                 colegios_service : ColegiosService = Depends(ColegiosService)) -> None:
        self.clases_repository = clases_respository
        self.colegios_service = colegios_service

    def crear_clase(self, clase_data: ClaseData) -> Clase:
        """
        Crea una clase
        """
        colegio = self.colegios_service.get_by_curso_id(clase_data.curso_codigo)
        clase = Clase(nombre=clase_data.nombre, descripcion=clase_data.descripcion, curso_codigo=clase_data.curso_codigo,
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

    def get_by_curso_id(self, curso_codigo: int) -> list:
        """
        Devuelve todas las clases de un curso
        """
        return self.clases_repository.get_by_curso_id(curso_codigo)
