def convertirAcelsius(valorFahrenheit):
    return (valorFahrenheit - 32) * 5 / 9

def convertirAfahrenheit(valorCelsius):
    return valorCelsius * 9 / 5 + 32

valor = float(input("ingrese el valor de temperatura: "))
escala = input("ingrese la escala original(celsius(C) o fahrenheit(F): ").upper()

if escala == "C":
    resultado = convertirAfahrenheit(valor)
    print(f"{valor}°C equivalen a {resultado}°F")
elif escala == "F":
    resultado = convertirAcelsius(valor)
    print(f"{valor}°F equivalen a {resultado}°C")
else:
    print("escala incorrecta, usa C para celsius o F para fahrenheit ! ")