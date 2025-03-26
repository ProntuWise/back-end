import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Carregar variáveis do .env
load_dotenv()

# Configuração via Pydantic Settings
class Settings(BaseSettings):
    AIVEN_URL: str
    PORT: str

    class Config:
        env_file = ".env"

settings = Settings(
    AIVEN_URL=os.getenv("AIVEN_URL"),
    PORT=os.getenv("PORT")
)

# Configuração do Banco de Dados
SQLALCHEMY_DATABASE_URL = settings.AIVEN_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True, 
    pool_pre_ping=True  
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependência para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
