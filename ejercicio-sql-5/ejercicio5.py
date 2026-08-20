from typing import List
from sqlalchemy import create_engine, String, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

# Creamos una base de datos nueva para este ejercicio
engine = create_engine("sqlite:///clases_curso.db", echo=False)

class Base(DeclarativeBase):
    pass

# 1. Modelo Curso actualizado
class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column(Integer)
    clases: Mapped[List["Clase"]] = relationship(back_populates="curso")

class Clase(Base):
    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(150))
    duracion_minutos: Mapped[int] = mapped_column(Integer)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped["Curso"] = relationship(back_populates="clases")

Base.metadata.create_all(engine)

with Session(engine) as session:
    curso_bd = Curso(titulo="bases de datos I", creditos=6)
    clase1 = Clase(tema="modelo generico de datos", duracion_minutos=120)
    clase2 = Clase(tema="modelo relacional de datos", duracion_minutos=120)
    clase3 = Clase(tema="transacciones", duracion_minutos=120)
    curso_bd.clases.extend([clase1, clase2, clase3])
    
    session.add(curso_bd)
    session.commit()

    print("\nclases del curso:")
    curso_guardado = session.query(Curso).filter_by(titulo="bases de datos I").first()
    
    if curso_guardado:
        print(f"CURSO: {curso_guardado.titulo} ({curso_guardado.creditos} creditos)")
        print("temario de clases:")
        for c in curso_guardado.clases:
            print(f" tema: {c.tema} | Duración: {c.duracion_minutos} min")
    else:
        print("No se encontró el curso buscado.")