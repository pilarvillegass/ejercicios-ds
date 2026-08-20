from typing import List
from sqlalchemy import create_engine, String, ForeignKey, Float, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine("sqlite:///reportes.db", echo=False)

class Base(DeclarativeBase):
    pass

class Profesor(Base):
    __tablename__ = "profesores"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")

class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped["Profesor"] = relationship(back_populates="cursos")
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="curso")

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante")

class Inscripcion(Base):
    __tablename__ = "inscripciones"
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)
    calificacion_final: Mapped[float] = mapped_column(Float, nullable=True)
    
    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")

Base.metadata.create_all(engine)

with Session(engine) as session:
    profe1 = Profesor(nombre="lucy")
    curso1 = Curso(titulo="epa", profesor=profe1)
    curso2 = Curso(titulo="ayp1", profesor=profe1)
    
    est1 = Estudiante(nombre="pilar")
    est2 = Estudiante(nombre="maria")
    
    session.add_all([
        Inscripcion(estudiante=est1, curso=curso1, calificacion_final=9.5),
        Inscripcion(estudiante=est1, curso=curso2, calificacion_final=8.0),
        Inscripcion(estudiante=est2, curso=curso1, calificacion_final=7.5)
    ])
    session.commit()

    print("\ncursos que da lucy")
    stmt_cursos = select(Curso).join(Curso.profesor).where(Profesor.nombre == "lucy")
    for curso in session.scalars(stmt_cursos):
        print(f" - {curso.titulo}")

    print("\npromedio de notas de pilar")
    stmt_promedio = select(func.avg(Inscripcion.calificacion_final)).join(Inscripcion.estudiante).where(Estudiante.nombre == "pilar")
    promedio_pilar = session.scalar(stmt_promedio)
    print(f" Promedio general: {promedio_pilar:.2f}")

    print("\ncantidad de alumnos por curso")
    stmt_conteo = select(Curso.titulo, func.count(Inscripcion.estudiante_id)).join(Curso.inscripciones).group_by(Curso.id)
    for titulo, cantidad in session.execute(stmt_conteo):
        print(f" - {titulo}: {cantidad} alumnos")