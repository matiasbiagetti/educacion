from fastapi import Depends
from pydantic import BaseModel

from app.models.colegio import Colegio
from app.repository.colegios_repository import ColegiosRepository


class ColegioData(BaseModel):
    nombre: str


class ColegiosService:
    """
    Colegios service
    """

    def __init__(self, colegios_repository: ColegiosRepository = Depends(ColegiosRepository)) -> None:
        self.colegios_repository = colegios_repository

    def crear_colegio(self, colegio_data: ColegioData) -> Colegio:
        """
        Crea un colegio
        """
        colegio = Colegio(nombre=colegio_data.nombre)
        self.colegios_repository.save(colegio)
        return colegio

    def get_by_curso(self, curso_codigo: int):
        """
        Devuelve el colegio de un curso
        """
        return self.colegios_repository.get_by_curso(curso_codigo)

    def obtener_colegios(self):
        """
        Devuelve todos los colegios
        """
        return self.colegios_repository.get_all()

    def obtener_colegio_que_comience_con(self, nombre_colegio: str):
        """
        Devuelve todos los colegios que contengan el nombre
        """
        return self.colegios_repository.get_that_starts_with(nombre_colegio)

    def obtener_colegio(self, id_colegio: int):
        """
        Devuelve un colegio
        """
        return self.colegios_repository.get_by_id(id_colegio)
