from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.curso import Curso


class CursosRepository:
    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, curso: Curso) -> None:
        self.session.add(curso)
        self.session.commit()

    def get_all(self) -> list:
        return self.session.query(Curso).all()

    def get_by_codigo(self, codigo: str) -> Curso:
        return self.session.query(Curso).filter(Curso.codigo == codigo).first()

    def get_by_profesor_id(self, profesor_id: int) -> list:
        return self.session.query(Curso).filter(Curso.profesor_id == profesor_id).all()

    def get_by_estudiante_id(self, estudiante_id: int) -> list:
        return self.session.query(Curso).filter(Curso.estudiantes.any(id=estudiante_id)).all()

    def add_student_to_course(self, curso_codigo: int) -> Curso:
        curso = self.session.query(Curso).filter(Curso.codigo == curso_codigo).first()

        self.session.commit()
        return curso

