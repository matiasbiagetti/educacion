from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.profesor import Profesor


class ProfesoresRepository:
    """
    Clase que interactua con la base de datos de profesores
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, profesor: Profesor) -> None:
        """
        Crea un profesor
        """
        self.session.add(profesor)
        self.session.commit()

    def get_all(self) -> list:
        """
        Devuelve todos los profesores
        """
        return self.session.query(Profesor).all()

    def get_by_id(self, id: int) -> Profesor:
        """
        Devuelve un profesor por su id
        """
        return self.session.query(Profesor).filter(Profesor.id == id).first()

    def get_by_curso_id(self, curso_codigo: int) -> list:
        """
        Devuelve todos los profesores de un curso
        """
        return self.session.query(Profesor).filter(Profesor.cursos.any(id=curso_codigo)).all()