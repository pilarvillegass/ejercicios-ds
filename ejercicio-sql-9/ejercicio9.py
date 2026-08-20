from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

engine = create_engine("sqlite:///transacciones.db", echo=False)

class Base(DeclarativeBase):
    pass

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))

class Inscripcion(Base):
    __tablename__ = "inscripciones"
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)

Base.metadata.create_all(engine)

def matricular_alumno(session: Session, est_id: int, cur_id: int):
    try:
        nueva_inscripcion = Inscripcion(estudiante_id=est_id, curso_id=cur_id)
        session.add(nueva_inscripcion)
        session.commit() 
        print(f" exito! alumno ID{est_id} matriculado en el curso ID {cur_id}")
        
    except IntegrityError:
        session.rollback() 
        print(f" ERROR: el alumno ya esta inscripto en este curso")
        
    except SQLAlchemyError as error_general:
        session.rollback()
        print(f" ERROR general en la base de datos: {error_general}")
 
with Session(engine) as session:

    est_pilar = Estudiante(id=20804, nombre="pilar")
    curso1 = Curso(id=123, titulo="algebra")
    
    session.add_all([est_pilar, curso1])
    session.commit() 

    print("\nmatriculamos por primera vez")
    matricular_alumno(session, est_id=20804, cur_id=123)

    print("\nmatriculamos de nuevo para ver el error")
    matricular_alumno(session, est_id=20804, cur_id=123)