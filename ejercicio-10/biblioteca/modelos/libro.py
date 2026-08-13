class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"{self.titulo} de {self.autor} (ISBN: {self.isbn}) - {estado}"