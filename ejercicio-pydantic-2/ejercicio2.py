from typing import Union, Literal
from pydantic import BaseModel, ValidationError


class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: Literal["sensor", "actuador", "gateway"]


dispositivo1 = Dispositivo(id_dispositivo=101, tipo="sensor")
print("instancia valida (id como int):")
print(dispositivo1)


dispositivo2 = Dispositivo(id_dispositivo="DISP-A22", tipo="actuador")
print("\ninstancia valida (id como str):")
print(dispositivo2)

try:
    Dispositivo(id_dispositivo=202, tipo="coso")
except ValidationError as error:
    print("\nerror por tipo invalido:")
    print(error)