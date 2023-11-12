from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.pregunta import Pregunta


class PreguntasRepository:
    """
    Clase para interactuar con la base de datos de preguntas
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, pregunta: Pregunta) -> None:
        """
        Crea una pregunta
        """
        self.session.add(pregunta)
        self.session.commit()

    def get_all(self) -> list:
        """
        Devuelve todas las preguntas
        """
        return self.session.query(Pregunta).all()

    def get_by_id(self, id: int) -> Pregunta:
        """
        Devuelve una pregunta por su id
        """
        return self.session.query(Pregunta).filter(Pregunta.id == id).first()

    def get_by_clase_id(self, clase_id: int) -> list:
        """
        Devuelve todas las preguntas de una clase
        """
        return self.session.query(Pregunta).filter(Pregunta.clase_id == clase_id).all()