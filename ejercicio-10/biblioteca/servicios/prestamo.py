from ..modelos.libro import Libro


def realizar_prestamo(libro):
    if libro.disponible:
        libro.disponible = False
        return f"prestamo realizado con exito: '{libro.titulo}'."
    else:
        return f"'{libro.titulo}' no se encuentra disponible."


def realizar_devolucion(libro):
    if not libro.disponible:
        libro.disponible = True
        return f"devolución realizada con exito: '{libro.titulo}'."
    else:
        return f"'{libro.titulo}' ya figuraba como disponible."


def consultar_disponibilidad(libro):
    if libro.disponible:
        return f"'{libro.titulo}' esta disponible para prestamo."
    else:
        return f"'{libro.titulo}' no este disponible (esta prestado)."