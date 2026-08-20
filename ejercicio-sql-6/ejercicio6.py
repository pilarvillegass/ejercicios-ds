from typing import List
from sqlalchemy import create_engine, String, ForeignKey, Integer, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine("sqlite:///inscripciones.db", echo=False)

class Base(DeclarativeBase):
    pass

inscripcion_table = Table(
    "inscripcion",
    Base.metadata,
    Column("estudiante_id", ForeignKey("estudiantes.id"), primary_key=True),
    Column("curso_id", ForeignKey("cursos.id"), primary_key=True),
)

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    legajo: Mapped[int] = mapped_column(Integer)
    cursos: Mapped[List["Curso"]] = relationship(
        secondary=inscripcion_table, back_populates="estudiantes"
    )

class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column(Integer)
    estudiantes: Mapped[List["Estudiante"]] = relationship(
        secondary=inscripcion_table, back_populates="cursos"
    )

Base.metadata.create_all(engine)

with Session(engine) as session:

    est1 = Estudiante(nombre="pilar", legajo=20804)
    est2 = Estudiante(nombre="maria", legajo=30704)

    curso1 = Curso(titulo="poo", creditos=5)
    curso2 = Curso(titulo="concurrencia", creditos=4)

    est1.cursos.extend([curso1, curso2]) 
    est2.cursos.append(curso1)            
    session.add_all([est1, est2])
    session.commit()

    print("\ninscriptos en poo")
    curso_bd = session.query(Curso).filter_by(titulo="poo").first()
    if curso_bd:
        for est in curso_bd.estudiantes:
            print(f" - {est.nombre} (Legajo: {est.legajo})")
    
    print("\ncursos en los que esta la estudiante pilar")
    pilar_bd = session.query(Estudiante).filter_by(nombre="pilar").first()
    if pilar_bd:
        for c in pilar_bd.cursos:
            print(f" - {c.titulo}")