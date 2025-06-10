
import bcrypt
from src.entities.user import User
from src.models.user import User as UserModel
from src.enums.user_type_enum import UserTypeEnum

class UserRepositoryMock:
  def __init__(self):
    self.users = [
      {
        "user_id": 1,
        "name": "John Doe",
        "email": "John@gmail.com",
        "password": "ajdbhfuy498u31br89341&*#Y$*@#oihfweo",
        "role": "Doctor",
        "is_active": True,
        "username": "JohnDoe",
        "is_first": True,
        "created_at": "2023-10-01T12:00:00Z"
      },
      {
        "user_id": 2,
        "name": "Jane Doe",
        "email": "Jane@gmail.com",
        "password": "ajdbhfuy498u31br89341&*#Y$*@#oihfweo",
        "role": "Doctor",
        "is_active": True,
        "username": "JaneDoe",
        "is_first": True,
        "created_at": "2023-10-01T12:00:00Z"
      },
    ]
  
  def createUser(self, user: User):
    try:
      # Simulate creating a user
      new_user = {
        "user_id": len(self.users) + 1,
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "role": user.role.value,
        "username": user.username,
        "is_active": True,
        "is_first": True,
        "created_at": "2023-10-01T12:00:00Z",
      }
      self.users.append(new_user)
      return True
    except Exception as e:
      raise Exception(f"Erro ao Criar Usuário: {e}")
    
  def getUserByIdentifier(self, identifier: str):
    try:
      # Simulate fetching a user by identifier (email or username)
      hashed_password = bcrypt.hashpw("senha123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
      for user in self.users:
        if user["email"] == identifier or user["username"] == identifier:
          return UserModel(
            user_id=user["user_id"],
            name=user["name"],
            email=user["email"],
            password=hashed_password,
            role=UserTypeEnum(user["role"]),
            is_active=user["is_active"],
            username=user["username"],
            is_first=user["is_first"],
            created_at=user["created_at"]
          )
      return None
    except Exception as e:
      raise Exception(f"Erro ao buscar usuário: {e}")
  
  def getUserById(self, user_id: int):
    try:
      for user in self.users:
        if user["user_id"] == user_id:
          return UserModel(
            user_id=user["user_id"],
            name=user["name"],
            email=user["email"],
            password=user["password"],
            role=UserTypeEnum(user["role"]),
            is_active=user["is_active"],
            username=user["username"],
            is_first=user["is_first"],
            created_at=user["created_at"]
          )
      return None
    except Exception as e:
      raise Exception(f"Erro ao buscar usuário: {e}")

  def updatePasswordUser(self, identifier: str, new_password: str):
    try:
      for user in self.users:
        if user["email"] == identifier or user["username"] == identifier:
          user["password"] = new_password
          return True
      return False
    except Exception as e:
      raise Exception(f"Erro ao atualizar senha: {e}")
  
  def deleteUser(self, user_id: int):
    try:
      for user in self.users:
        if user["user_id"] == user_id:
          self.users.remove(user)
          return True
      return False
    except Exception as e:
      raise Exception(f"Erro ao deletar usuário: {e}")
    