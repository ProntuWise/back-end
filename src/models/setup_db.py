from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, TIMESTAMP, Date
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

# Importando o dotenv para pegar a string de conexão
import os
from dotenv import load_dotenv
load_dotenv()
connect = os.getenv("CONNECT")

# Importando o caminho do certificado
caminho = os.path.abspath(os.path.join(os.getcwd(), './database/ca.pem'))

# Conexão
engine = create_engine(connect, echo=True, connect_args={'ssl': {'ca': caminho}})
# engine.execute(...)

# Sessão
Session = sessionmaker(bind=engine)
session = Session()

# Base
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(14), nullable=False, unique=True)
    crm = Column(String(15))
    tipo_user = Column(String(1), nullable=False)
    nome_user = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    senha = Column(String(200), nullable=False)
    finalizou_crianca = Column(Integer, default=0)

def cria_tabelas():
    Base.metadata.create_all(engine)