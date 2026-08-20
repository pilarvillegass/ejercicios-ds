from datetime import datetime
from typing import List
from sqlalchemy import create_engine, String, ForeignKey, Integer, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine("sqlite:///inscripciones_enriquecidas.db", echo=False)

class Base(DeclarativeBase):
    pass

class Inscripcion(Base):
    __tablename__ = "inscripciones"
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)
    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime)
    calificacion_final: Mapped[float] = mapped_column(Float, nullable=True) 

    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    legajo: Mapped[int] = mapped_column(Integer)
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante")

class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column(Integer)
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="curso")

Base.metadata.create_all(engine)

with Session(engine) as session:
    est_pilar = Estudiante(nombre="pilar", legajo=12345)
    curso_ing = Curso(titulo="ingenieria", creditos=5)
    
    nueva_inscripcion = Inscripcion(
        estudiante=est_pilar, 
        curso=curso_ing, 
        fecha_inscripcion=datetime.now(),
        calificacion_final=9.5
    )
    
    session.add(nueva_inscripcion)
    session.commit()

    print("\nnotas")
    pilar_bd = session.query(Estudiante).filter_by(nombre="pilar").first()
    
    if pilar_bd:
        print(f"la alumna: {pilar_bd.nombre} con legajo: {pilar_bd.legajo}")
        for insc in pilar_bd.inscripciones:
            print(f" en la materia: {insc.curso.titulo} tiene nota: {insc.calificacion_final}")