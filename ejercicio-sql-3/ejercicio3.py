from datetime import datetime
from typing import List
from sqlalchemy import create_engine, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine("sqlite:///bidireccional.db", echo=False)

class Base(DeclarativeBase):
    pass

class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    profesores: Mapped[List["Profesor"]] = relationship(back_populates="departamento")

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)

    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    
    departamento: Mapped["Departamento"] = relationship(back_populates="profesores")

Base.metadata.create_all(engine)

with Session(engine) as session:
    
    depto_ciencias = Departamento(nombre="historia")
    
    profe1 = Profesor(nombre="mar", email="mar@gmail.com", fecha_ingreso=datetime.now())
    profe2 = Profesor(nombre="martina", email="martina@gmail.com", fecha_ingreso=datetime.now())
    profe3 = Profesor(nombre="raul", email="raul@gmail.com", fecha_ingreso=datetime.now())
    
    depto_ciencias.profesores.extend([profe1, profe2, profe3])
    
    session.add(depto_ciencias)
    session.commit()

    print("\n departamento a profesores")
    depto_guardado = session.query(Departamento).first()
    for p in depto_guardado.profesores:
        print(f"el/la profe {p.nombre} pertenece al departamento {depto_guardado.nombre}")

    print("\nprofesor a departamento")
    profe_guardado = session.query(Profesor).filter_by(nombre="mar").first()
    print(f"buscando a mar y verificando departamento: {profe_guardado.departamento.nombre}")