from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

connect = os.getenv("AIVEN_URL")

# Caminho do certificado SSL
caminho = './scripts/ca.pem'
caminho_completo = os.path.abspath(os.path.join(os.getcwd(), caminho))

engine = create_engine(
    connect,
    echo=True,
    connect_args={"ssl": {"ca": caminho_completo}}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
