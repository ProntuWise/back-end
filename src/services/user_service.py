import bcrypt
from datetime import datetime
from src.repositories.user_repository import UserRepository
from src.entities.user import CreateUserRequest, User
class UserServices():
  def createUser(self, user: CreateUserRequest):
    repo = UserRepository()
    try:
      # Validate user data
      if not user.name or not user.email or not user.role:
        raise ValueError("All fields are required")
      password = user.name + datetime.now().strftime("%d%m%Y")

      hash_password = password.encode('utf-8')
      hash_password = bcrypt.hashpw(hash_password, bcrypt.gensalt())

      # Create user object
      user = User(user.name, user.email, hash_password, user.role)
      print(user)
      repo.createUser(user)
      return user
    except Exception as e:
      raise Exception(f"Erro ao Criar Usuário: {e}")