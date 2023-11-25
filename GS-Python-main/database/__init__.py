from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import inspect


SQLALCHEMY_DATABASE_URL = "oracle+oracledb://rm552243:250904@oracle.fiap.com.br/?service_name=orcl"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False, 
    autocommit=False, 
    # expire_on_commit=False
)

Base = declarative_base()
#Define a context manager for database sessions.
#Define um gerenciador de contexto para sessões de banco de dados.
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

#Create database tables based on models.
#Crie tabelas de banco de dados com base nos modelos.




def create_tables():
    Base.metadata.create_all(engine)