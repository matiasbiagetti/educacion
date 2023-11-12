from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.opcion import Opcion


class OpcionesRepository:
    """
    Clase para interactuar con la base de datos de opciones
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, opcion: Opcion) -> None:
        """
        Crea una opcion
        """
        self.session.add(opcion)
        self.session.commit()

    def get_all(self) -> list:
        """
        Devuelve todas las opciones
        """
        return self.session.query(Opcion).all()

    def get_by_id(self, id: int) -> Opcion:
        """
        Devuelve una opcion por su id
        """
        return self.session.query(Opcion).filter(Opcion.id == id).first()

    def get_by_pregunta_id(self, pregunta_id: int) -> list:
        """
        Devuelve todas las opciones de una pregunta
        """
        return self.session.query(Opcion).filter(Opcion.pregunta_id == pregunta_id).all()