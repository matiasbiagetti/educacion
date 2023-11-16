from fastapi import Depends
from pydantic import BaseModel

from app.models.curso import Curso
from app.repository.cursos_repository import CursosRepository


class CursoData(BaseModel):
    codigo: int
    materia: str
    profesor_id: int
    colegio_id: int
    anio_cursado: int
    division: str


class CursosService:
    def __init__(self, cursos_repository: CursosRepository = Depends(CursosRepository)) -> None:
        self.cursos_repository = cursos_repository

    def crear_curso(self, curso_data: CursoData) -> Curso:
        curso = Curso(
            codigo=curso_data.codigo,
            materia=curso_data.materia,
            profesor_id=curso_data.profesor_id,
            colegio_id=curso_data.colegio_id,
            anio_cursado=curso_data.anio_cursado,
            division=curso_data.division
        )

        self.cursos_repository.save(curso)
        return curso

    def obtener_curso(self, codigo: str) -> Curso:
        return self.cursos_repository.get_by_codigo(codigo)

    def obtener_cursos(self) -> list[Curso]:
        return self.cursos_repository.get_all()

    def obtener_cursos_por_profesor(self, profesor_id: int) -> list[Curso]:
        return self.cursos_repository.get_by_profesor_id(profesor_id)

    def obtener_cursos_por_estudiante(self, estudiante_id: int) -> list[Curso]:
        return self.cursos_repository.get_by_estudiante_id(estudiante_id)

    def agregar_alumno_a_curso(self, id_curso: int, id_estudiante: int) -> Curso:
        return self.cursos_repository.add_student_to_course(id_curso, id_estudiante)
