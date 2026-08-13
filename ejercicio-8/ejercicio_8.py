def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):
    if precio_base < 0 or porcentaje_descuento < 0:
        raise ValueError("el precio base y el porcentaje de descuento tienen que ser positivos.")

    precio_con_descuento = precio_base * (1 - porcentaje_descuento / 100)

    if es_vip:
        precio_con_descuento = precio_con_descuento * (1 - 5 / 100)

    return precio_con_descuento

try:
    resultado1 = calcular_precio_final(1000)
    print(f"Precio final (sin VIP, descuento default): ${resultado1:.2f}")

    resultado2 = calcular_precio_final(1500, porcentaje_descuento=20, es_vip=True)
    print(f"Precio final (VIP, 20% descuento): ${resultado2:.2f}")

    resultado3 = calcular_precio_final(-200)
    print(f"Precio final: ${resultado3:.2f}")
except ValueError as error:
    print(f"Error: {error}")