from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

# Carrega a URL de conexão do banco
connect = os.getenv("AIVEN_URL")

# Caminho do certificado SSL
caminho = './scripts/ca.pem'
caminho_completo = os.path.abspath(os.path.join(os.getcwd(), caminho))

# Cria o engine de conexão
engine = create_engine(connect, echo=True, connect_args={'ssl': {'ca': caminho_completo}})

# Cria uma classe para gerenciar as sessões
class Conexao:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def fecha_conexao(self):
        self.session.close()
        engine.dispose()

    def get_conexao(self):
        return self.session
