from pydantic import BaseModel, EmailStr, Field, ValidationError

class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_acceso: int = Field(ge=1, le=5)

try:
    usuario = UsuarioSistema(email="email-novalido", nivel_acceso=9) #2 errores
except ValidationError as error:
    print("errores en la validacion:")
    print(error)