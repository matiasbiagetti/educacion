from sqlalchemy import ForeignKey, Integer, Column, Table

from app.models.base_model import EntityMeta

estudiantes_cursos = Table('alumnos_cursos', EntityMeta.metadata,
                           Column('alumno_id', ForeignKey('alumnos.id'), primary_key=True),
                           Column('curso_id', ForeignKey('cursos.id'), primary_key=True)
                           )

