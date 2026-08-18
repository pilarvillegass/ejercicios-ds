from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

class PerfilUsuario(BaseModel):
    username: str = Field(pattern=r"^[a-z0-9_]{3,20}$")
    biografia: Optional[str] = Field(default=None, max_length=200)
    redes_sociales: Optional[List[str]] = None

perfil1 = PerfilUsuario(
    username="pilarvillegass",
    biografia="estudiante, 22 años",
    redes_sociales=["https://github.com/pilarvillegass", "@thisispurin"]
)
print("instnacia valida:")
print(perfil1)

try:
    PerfilUsuario(username="Pilar-Villegass!", biografia="bio corta") #usuario invalido
except ValidationError as error:
    print("\nerror por usuario invalido:")
    print(error)

try:
    PerfilUsuario(username="pilar_villegas", biografia="holaaaaa" * 250) #bio muyyy larga
except ValidationError as error:
    print("\nerror bio demasiado larga:")
    print(error)