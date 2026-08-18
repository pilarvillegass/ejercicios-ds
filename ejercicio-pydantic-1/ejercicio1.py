from pydantic import BaseModel, Field, EmailStr, ValidationError


class Estudiante(BaseModel):
    legajo: int = Field(gt=0)
    nombre_completo: str = Field(min_length=5)
    email: EmailStr
    promedio: float = Field(ge=0.0, le=10.0, default=0.0)


estudiante_valido = Estudiante(
    legajo=1234,
    nombre_completo="pilar villegas",
    email="pilar@gmail.com",
    promedio=7.5
)
print("instancia valida creada:")
print(estudiante_valido)

try:
    Estudiante(legajo=-5, nombre_completo="pilar villegas", email="pilar@gmail.com")
except ValidationError as error:
    print("\nerror por legajo negativo:")
    print(error)

try:
    Estudiante(legajo=1234, nombre_completo="pi", email="pilar@gmail.com")
except ValidationError as error:
    print("\nerror por nombre muy corto:")
    print(error)

try:
    Estudiante(legajo=1234, nombre_completo="pilar villegas", email="mail-invalido")
except ValidationError as error:
    print("\nerror por email invalido:")
    print(error)


try:
    Estudiante(legajo=1234, nombre_completo="pilar villegas", email="pilar@gmail.com", promedio=20.0)
except ValidationError as error:
    print("\nerror por promedio fuera de rango:")
    print(error)
    