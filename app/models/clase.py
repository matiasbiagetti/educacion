from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta


class Clase(EntityMeta):
    """
    Una clase es una clase de un curso, puede tener las propuestas generadas por la IA y tiene
    temas espedificos que se enseñaran esa clase
    """

    __tablename__ = "clases"

    id = Column(Integer, primary_key=True)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    tema = Column(String(100), nullable=False)

    curso = relationship("Curso", back_populates="clases")
    propuestas = relationship("Propuesta", back_populates="clase")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "curso": self.curso.to_dict(),
            "tema": self.tema,
            "propuestas": [propuesta.to_dict() for propuesta in self.propuestas],
        }
