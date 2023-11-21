import openai
from fastapi import Depends

from app.models.curso import Curso
from app.services.cursos_service import CursosService
from app.services.estudiantes_service import EstudiantesService
from app.services.respuestas_service import RespuestasService
import os
from dotenv import load_dotenv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

openai.api_key  = os.getenv("OPENAI_API_KEY")
class OpenAIService:
    def __init__(self, cursos_service: CursosService = Depends(CursosService),
                 estudiantes_service: EstudiantesService = Depends(EstudiantesService),
                 respuestas_service: RespuestasService = Depends(RespuestasService)):
        self.cursos_service = cursos_service
        self.estudiantes_service = estudiantes_service
        self.respuestas_service = respuestas_service



    def crear_propuesta(self, curso_codigo: int, tema: str, tipo: str):
        """
        Crea una propuesta de clase en base a un tema un tipo y una materia
        """

        curso = self.cursos_service.obtener_curso(curso_codigo)
        texto = self.generar_prompt(curso, tema, tipo)

        completion = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=texto,
            max_tokens=1000
        )

        return completion["choices"][0]["text"]

    def generar_prompt(self, curso: Curso, tema: str, tipo: str):
        """
        Genera un texto de ejemplo en base a un curso
        """
        cant_estudiantes = len(self.estudiantes_service.obtener_estudiantes_por_curso(curso.codigo))

        contexto = f"Contexto: Eres el asistente de un profesor de escuela secundaria de {curso.anio_cursado} año. " \
                   f"El profesor te pide que le brindes 2 opciones de {tipo} para una clase donde se dictara el tema {tema}" \
                   f" en la materia {curso.materia}. " \

        if tipo == "didacticas" or tipo == "herramientas":
            contexto += f"En el curso hay {cant_estudiantes} estudiantes. Tene en cuenta eso a la hora de plantear dinamicas para hacer durante la clase." \

        if tipo == "herramientas":
            contexto += f"Porfavor da herramientas especificas (especifica el nombre de la herramienta como Kahoot, Mentimeter, algun simulador, Miro, etc) para sedimentar el conocimiento despues de la clase o para alguna demostracion"


        if tipo == "ejemplos":
            contexto += f"Porfavor da 3 ejemplos especificos y la explicacion donde se aplique el tema de {tema} en la vida real. Intenta dar ejemplos solamente basados en las caracteristicas y gustos del curso mencionadas en general. Solamente enumerarlos y explicarlos"

        contexto += f"A continuacion te detallare algunas preguntas y las respuestas que dieron los alumnos para que " \
                    f"tengas mas contexto sobre el curso. Si la respuesta esta repetida es porque fue esa la respuesta la cantidad de veces que se repita." \

        for pregunta in curso.preguntas:
            respuestas = self.respuestas_service.obtener_respuestas_a_pregunta(curso.codigo, pregunta.id)
            respuestas_string = ', '.join(respuestas)
            pregunta_final = f"\nPregunta: {pregunta.texto}\nRespuestas: {respuestas_string} ;"
            contexto += pregunta_final

        print(contexto)

        return contexto
