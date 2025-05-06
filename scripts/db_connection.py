from scripts.session import SessionLocal, engine

class Conexao:
    def __init__(self):
        self.session = SessionLocal()

    def fecha_conexao(self):
        self.session.close()
        engine.dispose()

    def get_conexao(self):
        return self.session
