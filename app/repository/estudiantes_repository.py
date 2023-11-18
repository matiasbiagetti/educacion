from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.estudiante import Estudiante


class EstudiantesRepository:
    """
    Clase para interactuar con la base de datos de estudiantes
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, estudiante: Estudiante) -> None:
        """
        Crea un estudiante
        """
        self.session.add(estudiante)
        self.session.commit()

    def get_all(self) -> list:
        """
        Devuelve todos los estudiantes
        """
        return self.session.query(Estudiante).all()

    def get_by_id(self, id: int) -> Estudiante:
        """
        Devuelve un estudiante por su id
        """
        return self.session.query(Estudiante).filter(Estudiante.id == id).first()

    def get_by_curso_id(self, curso_id: int) -> list:
        """
        Devuelve todos los estudiantes de un curso
        """
        return self.session.query(Estudiante).filter(Estudiante.cursos.any(id=curso_id)).all()
