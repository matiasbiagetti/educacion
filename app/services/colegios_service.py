from pydantic import BaseModel


class ColegioData(BaseModel):
    nombre: str

class ColegiosService:
    """
    Colegios service
    """
    def __init__(self, colegios_repository) -> None:
        self.colegios_repository = colegios_repository

    def crear_colegio(self, colegio_data: ColegioData) -> Colegio:
        """
        Crea un colegio
        """
        return self.colegios_repository.crear_colegio(colegio_data)
