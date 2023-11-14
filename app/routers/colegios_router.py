from http import HTTPStatus

from fastapi import HTTPException, APIRouter, Depends
from pydantic import BaseModel

from app.services.colegios_service import ColegiosService, ColegioData

colegios_router = APIRouter(prefix="/colegios", tags=["Colegios"])


class ColegioPayload(BaseModel):
    nombre: str


class ColegioResponse(ColegioPayload):
    id: int


@colegios_router.post("/", status_code=HTTPStatus.CREATED, response_model=ColegioResponse)
def crear_colegio(payload: ColegioPayload, service: ColegiosService = Depends(ColegiosService)):
    """
    Crea un colegio
    """
    try:
        data = ColegioData(nombre=payload.nombre)
        colegio = service.crear_colegio(data)
        return ColegioResponse(id=colegio.id, nombre=colegio.nombre)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

@colegios_router.get("/{nombre_colegio}", response_model=ColegioResponse)
def obtener_colegio(nombre_colegio: str, service: ColegiosService = Depends(ColegiosService)):
    """
    Obtiene un colegio
    """
    try:
        colegio = service.obtener_colegio(nombre_colegio)
        return ColegioResponse(**colegio)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

@colegios_router.get("/", response_model=list[ColegioResponse])
def obtener_colegios(service: ColegiosService = Depends(ColegiosService)):
    """
    Obtiene todos los colegios
    """
    try:
        colegios = service.obtener_colegios()
        return [ColegioResponse(**colegio) for colegio in colegios]
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

# endpoint that recieves by query param part of the name of the school and returns a list of schools that match the query, it will have many requests because is a searchbar in the frontend
@colegios_router.get("/search/{nombre_colegio}", response_model=list[ColegioResponse])
def obtener_colegios_por_nombre(nombre_colegio: str, service: ColegiosService = Depends(ColegiosService)):
    """
    Obtiene todos los colegios que contengan el nombre
    """
    try:
        colegios = service.obtener_colegios_por_nombre(nombre_colegio)
        return [ColegioResponse(**colegio) for colegio in colegios]
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


