from sqlalchemy import Column, ForeignKey, Table, Integer
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta

class PreguntaCurso(EntityMeta):
    __tablename__ = 'preguntas_cursos'
    pregunta_id = Column(Integer, ForeignKey('preguntas.id'), primary_key=True)
    curso_id = Column(Integer, ForeignKey('cursos.codigo'), primary_key=True)

    # Define relationships


    def to_dict(self) -> dict:
        return {
            "pregunta": self.pregunta.to_dict(),
            "curso": self.curso.to_dict(),
        }