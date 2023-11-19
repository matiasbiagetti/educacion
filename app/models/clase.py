from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta
from app.models.propuesta import Propuesta
from app.models.curso import Curso


class Clase(EntityMeta):
    __tablename__ = 'clases'
    id = Column(Integer, primary_key=True)
    curso_codigo = Column(Integer, ForeignKey('cursos.codigo'), nullable=False)
    tema = Column(String(length=100), nullable=False)

    # Define the relationship with the 'cursos' table
    curso = relationship('Curso', back_populates='clases')
    propuestas = relationship('Propuesta', back_populates='clase')

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "curso": self.curso.to_dict(),
            "tema": self.tema,
        }
