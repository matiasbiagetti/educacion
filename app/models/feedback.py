from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta


class Feedback(EntityMeta):
    """
    Un feedback es una opinion de un estudiante sobre un curso
    """
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    texto = Column(String(length=255), nullable=False)
    curso_codigo = Column(Integer, ForeignKey('cursos.codigo'), nullable=False)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), nullable=False)
    clasificacion = Column(String(length=255), nullable=False)

    # Define relationships
    curso = relationship('Curso', back_populates='feedback')
    estudiante = relationship('Estudiante', back_populates='feedback')

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "texto": self.texto,
            "curso": self.curso.to_dict(),
            "alumno": self.alumno.to_dict(),
            "clasificacion": self.clasificacion,
        }
