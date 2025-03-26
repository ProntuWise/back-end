from db_connection import Conexao

def test_connection():
    try:
        conexao = Conexao()
        print("Conexão estabelecida com sucesso!")
        conexao.fecha_conexao()
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")

if __name__ == "__main__":
    test_connection()
