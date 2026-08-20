from datetime import datetime
from typing import List
from sqlalchemy import create_engine, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine("sqlite:///cursos.db", echo=False)

class Base(DeclarativeBase):
    pass

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)
    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")

class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column(Integer)
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped["Profesor"] = relationship(back_populates="cursos")

Base.metadata.create_all(engine)

with Session(engine) as session:
    profecurso = Profesor(nombre="marcelo", email="marcelo@gmail.com", fecha_ingreso=datetime.now())
    curso_lab = Curso(titulo="laboratorio de program. y lenguajes", creditos=5)
    curso_apu = Curso(titulo="APU", creditos=4)
    profecurso.cursos.extend([curso_lab, curso_apu])
    
    session.add(profecurso)
    session.commit()

    print("\n cursos dictados")
    profe_guardado = session.query(Profesor).filter_by(nombre="marcelo").first()
    print(f"profesor: {profe_guardado.nombre}")
    for curso in profe_guardado.cursos:
        print(f" - {curso.titulo} | otorga:{curso.creditos} creditos")
        

    print("\n profesor asignado al curso")
    curso_guardado = session.query(Curso).filter_by(titulo="laboratorio de program. y lenguajes").first()
    print(f"el curso de {curso_guardado.titulo} es dictado por {curso_guardado.profesor.nombre}")