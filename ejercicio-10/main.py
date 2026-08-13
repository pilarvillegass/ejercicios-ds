from biblioteca.modelos.libro import Libro
from biblioteca.servicios.prestamo import (
    realizar_prestamo,
    realizar_devolucion,
    consultar_disponibilidad,
)

libro1 = Libro("teoria de la computacion", "j glenn brookshear", "978-0307350438")
libro2 = Libro("el principito", "saint exupery", "978-0451524935")

print(libro1)
print(libro2)

print("\ncaso de uso ")

print(consultar_disponibilidad(libro1))

print(realizar_prestamo(libro1))
#intentamos hacer prestamo pero ya esta prestado
print(realizar_prestamo(libro1))
#consultamos
print(consultar_disponibilidad(libro1))
#lo devolvemos
print(realizar_devolucion(libro1))
#aca nos deberia decir q ya esta disponible
print(realizar_devolucion(libro1))

print(libro1)
print(libro2)