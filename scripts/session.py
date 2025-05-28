from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Removendo o ssl-mode da string de conexão
connect = os.getenv("AIVEN_URL").replace("?ssl-mode=REQUIRED", "")

print("String de conexão:", connect)

engine = create_engine(
    connect,
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

