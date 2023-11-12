from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.propuesta import Propuesta


class PropuestasRepository:
    """
    Clase para interactuar con la base de datos de propuestas
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, propuesta: Propuesta) -> None:
        """
        Crea una propuesta
        """
        self.session.add(propuesta)
        self.session.commit()

    def get_all(self) -> list:
        """
        Devuelve todas las propuestas
        """
        return self.session.query(Propuesta).all()

    def get_by_id(self, id: int) -> Propuesta:
        """
        Devuelve una propuesta por su id
        """
        return self.session.query(Propuesta).filter(Propuesta.id == id).first()

    def get_by_curso_id(self, curso_id: int) -> list:
        """
        Devuelve todas las propuestas de un curso
        """
        return self.session.query(Propuesta).filter(Propuesta.curso_id == curso_id).all()