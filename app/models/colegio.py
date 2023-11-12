from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta


class Colegio(EntityMeta):
    """
    Un colegio es una institución educativa
    """

    __tablename__ = "colegios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    cursos = relationship("Curso", back_populates="colegio")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
        }