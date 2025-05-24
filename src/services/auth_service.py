import jwt
import bcrypt
from datetime import datetime, timedelta
from src.mock.user_repository_mock import UserRepositoryMock
from src.repositories.user_repository import UserRepository

class AuthService:
  def __init__(self, repo: UserRepository | UserRepositoryMock):
    self.repo = repo

  def login(self, identifier: str, password: str):
    try:
      # buscar usuário pelo identificador (email ou username)
      user = self.repo.getUserByIdentifier(identifier)
      if not user:
        raise Exception("Usuário não encontrado")

      if user.is_first:
        return "is_first"
      # verificar se a senha está correta
      if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        print("Senha incorreta")
        raise Exception("Senha incorreta")
      
      # gerar token JWT
      token = jwt.encode(
        {
          "user_id": user.user_id,
          "username": user.username,
          "role": user.role.value,
          "exp": datetime.now() + timedelta(hours=2)
        },
        "secret_key",
        algorithm="HS256"
      )

      return token
    except Exception as e:
      raise Exception(f"Erro ao Criar Usuário: {e}")