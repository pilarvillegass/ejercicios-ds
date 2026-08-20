from datetime import datetime
from sqlalchemy import create_engine, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///profesores.db", echo=False)

class Base(DeclarativeBase):
    pass

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)

   
    def __repr__(self) -> str:
        return f"Profesor(id={self.id}, nombre='{self.nombre}', email='{self.email}')"

Base.metadata.create_all(engine)

with Session(engine) as session:
    
    profe1 = Profesor(nombre="lucy", email="lucy@gmial.com", fecha_ingreso=datetime.now())
    profe2 = Profesor(nombre="sebastian", email="sebastian@email.com", fecha_ingreso=datetime.now())
    
    session.add_all([profe1, profe2])
    session.commit()
    
    print("\n lista de profes en la base")
    profesores_guardados = session.query(Profesor).all()
    for prof in profesores_guardados:
        print(prof)