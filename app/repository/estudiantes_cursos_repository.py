from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.estudiantes_cursos import EstudianteCurso


class EstudiantesCursosRepository:
    """
    Clase para interactuar con la base de datos de estudiantes
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, estudiante_curso: EstudianteCurso) -> None:
        """
        Crea un estudiante
        """
        self.session.add(estudiante_curso)
        self.session.commit()

    def get_by_curso_codigo(self, curso_codigo: int) -> List[EstudianteCurso]:
        """
        Obtiene todos los estudiantes
        """
        return self.session.query(EstudianteCurso).filter(EstudianteCurso.curso_codigo == curso_codigo).all()