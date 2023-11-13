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
    def __init__(self, colegios_repository : ColegiosRepository = Depends(ColegiosRepository)) -> None:
        self.colegios_repository = colegios_repository

    def crear_colegio(self, colegio_data: ColegioData) -> Colegio:
        """
        Crea un colegio
        """
        colegio = Colegio(nombre=colegio_data.nombre)
        self.colegios_repository.save(colegio)
        return colegio
