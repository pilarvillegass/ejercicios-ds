from typing import Annotated, Optional
from pydantic import BaseModel, Field, ValidationError

CoordenadaGPS = Annotated[float, Field(ge=-90.0, le=90.0)]


class Ubicacion(BaseModel):
    longitud: CoordenadaGPS
    latitud: CoordenadaGPS
    etiqueta: Optional[str] = None


ubicacion1 = Ubicacion(longitud=-58.3816, latitud=-34.6037, etiqueta="dentro del rango")
print("instancia valida:")
print(ubicacion1)

try:
    Ubicacion(longitud=10.0, latitud=120.0, etiqueta="fuera de rango")
except ValidationError as error:
    print("\nerror latitud fuera de rango:")
    print(error)