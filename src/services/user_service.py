import bcrypt
from datetime import datetime
from fastapi import HTTPException
from src.repositories.user_repository import UserRepository
from src.mock.user_repository_mock import UserRepositoryMock
from src.entities.user import CreateUserRequest, User

class UserServices:
  def __init__(self, repo: UserRepository | UserRepositoryMock):
      self.repo = repo

  def createUser(self, user: CreateUserRequest) -> User:
    try:
      # Validação básica
      if not user.name or not user.email or not user.role:
          raise HTTPException(status_code=422, detail="Todos os campos são obrigatórios")

      # Gerar senha inicial baseada no nome + data
      password = user.name + datetime.now().strftime("%d%m%Y")

      # Hash da senha
      hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

      # Criar objeto User
      new_user = User(
          name=user.name,
          email=user.email,
          password=hash_password,
          role=user.role
      )

      # Persistir no banco
      self.repo.createUser(new_user)
      return new_user
    except Exception as e:
      raise Exception(f"Erro ao Criar Usuário: {e}")
