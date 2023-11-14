from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta
from app.models.curso import Curso


class Colegio(EntityMeta):
    __tablename__ = 'colegios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(length=100), nullable=False, unique=True)

    cursos = relationship('Curso', back_populates='colegio')

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cursos": [curso.to_dict() for curso in self.cursos],
        }