from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta


class Feedback(EntityMeta):
    """
    Un feedback es una opinion de un estudiante sobre un curso
    """

    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)
    texto = Column(String(255), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    alumno_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=False)
    clasificacion = Column(String(255), nullable=False)

    curso = relationship("Curso", back_populates="feedback")
    alumno = relationship("Alumno", back_populates="feedback")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "texto": self.texto,
            "curso": self.curso.to_dict(),
            "alumno": self.alumno.to_dict(),
            "clasificacion": self.clasificacion,
        }