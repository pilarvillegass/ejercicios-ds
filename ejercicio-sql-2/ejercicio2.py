from datetime import datetime
from typing import List
from sqlalchemy import create_engine, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine("sqlite:///departamentos.db", echo=False)

class Base(DeclarativeBase):
    pass

class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    profesores: Mapped[List["Profesor"]] = relationship()
    def __repr__(self) -> str:
        return f"departamento: ID={self.id} | nombre={self.nombre}"

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)

    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))

    def __repr__(self) -> str:
        return f"profesor: nombre={self.nombre} | depto ID={self.departamento_id}"

Base.metadata.create_all(engine)

with Session(engine) as session:
    depto_sistemas = Departamento(nombre="sistemas")
    
    profe1 = Profesor(nombre="lucy", email="lucy@gmail.com", fecha_ingreso=datetime.now())
    profe2 = Profesor(nombre="sebastian", email="sebastian@email.com", fecha_ingreso=datetime.now())
    
    depto_sistemas.profesores.append(profe1)
    depto_sistemas.profesores.append(profe2)

    session.add(depto_sistemas)
    session.commit()

    print("\nconsultando departamentos..")
    depto_guardado = session.query(Departamento).first()
    print(depto_guardado)
    
    print(f"\nprofesores del departamento de {depto_guardado.nombre}")
    for prof in depto_guardado.profesores:
        print(prof)