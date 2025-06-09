import jwt
import bcrypt
from datetime import datetime, timedelta
from src.mock.user_repository_mock import UserRepositoryMock
from src.repositories.user_repository import UserRepository
import time

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
      expiration = datetime.utcnow() + timedelta(hours=2)
      exp_timestamp = int(expiration.timestamp())
      
      print("Tempo atual UTC:", datetime.utcnow())
      print("Tempo expiração:", expiration)
      print("Timestamp expiração:", exp_timestamp)
      
      token = jwt.encode(
        {
          "user_id": user.user_id,
          "username": user.username,
          "role": user.role.value,
          "exp": exp_timestamp
        },
        "secret_key",
        algorithm="HS256"
      )

      return token
    except Exception as e:
      raise Exception(f"Erro ao Criar Usuário: {e}")