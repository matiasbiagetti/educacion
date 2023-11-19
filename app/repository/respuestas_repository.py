from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.estudiante import Estudiante
from app.models.respuesta import Respuesta


class RespuestasRepository:
    """
    Clase para interactuar con la base de datos de respuestas
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, respuesta: Respuesta) -> None:
        """
        Crea una respuesta
        """
        self.session.add(respuesta)
        self.session.commit()

    def get_all(self) -> list:
        """
        Devuelve todas las respuestas
        """
        return self.session.query(Respuesta).all()

    def get_by_id(self, id: int) -> Respuesta:
        """
        Devuelve una respuesta por su id
        """
        return self.session.query(Respuesta).filter(Respuesta.id == id).first()

    def get_by_estudiante_id(self, estudiante_id: int) -> list:
        """
        Devuelve todas las respuestas de un estudiante
        """
        return self.session.query(Respuesta).filter(Respuesta.estudiante_id == estudiante_id).all()

    def get_by_pregunta_id(self, pregunta_id: int) -> list:
        """
        Devuelve todas las respuestas de una pregunta
        """
        return self.session.query(Respuesta).filter(Respuesta.pregunta_id == pregunta_id).all()

    def get_by_pregunta_id_and_curso_codigo(self, pregunta_id: int, curso_codigo: int) -> list:
        """
        Devuelve todas las respuestas de una pregunta y un curso
        """
        return self.session.query(Respuesta).filter(Respuesta.pregunta_id == pregunta_id,
                                                    Respuesta.estudiante_id == Estudiante.id, Estudiante.cursos.any(id=curso_codigo)).all()


