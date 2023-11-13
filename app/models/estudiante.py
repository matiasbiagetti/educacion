from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


from app.models.base_model import EntityMeta
from app.models.estudiantes_cursos import estudiantes_cursos


class Estudiante(EntityMeta):
    """
    Un Estudiante es una persona que asiste a un curso
    """

    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)

    cursos = relationship("Curso", secondary=estudiantes_cursos, back_populates="estudiantes")
    respuestas = relationship("Respuesta", back_populates="estudiantes")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_nacimiento": self.fecha_nacimiento.strftime("%d/%m/%Y"),
            "cursos": [curso.to_dict() for curso in self.cursos],
            "respuestas": [respuesta.to_dict() for respuesta in self.respuestas],
        }
