contrasenia = input("ingrese una contraseña:")

tieneMayuscula = any (char.isupper() for char in contrasenia)
tieneMinuscula = any (char.islower() for char in contrasenia)
tieneLongitud = len(contrasenia) >= 8

if tieneLongitud and tieneMayuscula and tieneMinuscula:
    print("contraseña valida")
else:
    print("contraseña invalida")
    if not tieneLongitud:
        print("la contraseña debe tener al menos 8 caracteres")
    if not tieneMayuscula:
        print("la contraseña debe tener al menos una letra mayuscula")
    if not tieneMinuscula:
        print("la contraseña debe tener al menos una letra minuscula")
        