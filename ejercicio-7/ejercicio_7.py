def analizar_temperaturas(registros):
    valorMAX = max(registros)
    valorMIN = min(registros)
    promedio = sum(registros) / len(registros)
    return (valorMAX, valorMIN, promedio)

temperaturasDePrueba = [15, 10, 18, 25, 30, 20]

maximo, minimo, promedio = analizar_temperaturas(temperaturasDePrueba)

print(f"Temperatura máxima: {maximo}°C")
print(f"Temperatura mínima: {minimo}°C")
print(f"Promedio: {promedio:.2f}°C")