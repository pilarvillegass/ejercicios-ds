CONTRASENIA = "Admin1234"
intentosMAX = 3
intentos = 0
esCorrecta = False

while intentos < intentosMAX:
    intento = input("Ingrese la contraseña: ")
    intentos += 1
    if intento == CONTRASENIA:
        esCorrecta = True
        break
    else:
        intentosRestantes = intentosMAX - intentos
        print(f"contraseña incorrecta. te quedan: {intentosRestantes} intentos")

if esCorrecta:
        print("inicio de sesion exitoso")
else:
        print("se agotaron los intentos, cuenta bloqueada")