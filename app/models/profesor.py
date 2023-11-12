from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Profesor(EntityMeta):
    """
    Un profesor es una persona que enseña en un curso
    """

    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    cursos = relationship("Curso", back_populates="profesor")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cursos": [curso.to_dict() for curso in self.cursos],
        }