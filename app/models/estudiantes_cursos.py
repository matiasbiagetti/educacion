from sqlalchemy import ForeignKey, Integer, Column, Table
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta


class EstudianteCurso(EntityMeta):
    __tablename__ = 'estudiantes_cursos'
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), primary_key=True)
    curso_codigo = Column(Integer, ForeignKey('cursos.codigo'), primary_key=True)


    def to_dict(self) -> dict:
        return {
            "estudiante": self.estudiante.to_dict(),
            "curso": self.curso.to_dict(),
        }
