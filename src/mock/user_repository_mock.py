from src.entities.user import User

class UserRepositoryMock:
  def __init__(self):
    self.users = [
      {
        "id": 1,
        "name": "John Doe",
        "email": "John@gmail.com",
        "password": "ajdbhfuy498u31br89341&*#Y$*@#oihfweo",
        "role": "Doctor",
        "is_active": True,
        "username": "JohnDoe",
        "is_first": False,
        "created_at": "2023-10-01T12:00:00Z"
      },
      {
        "id": 2,
        "name": "Jane Doe",
        "email": "Jane@gmail.com",
        "password": "ajdbhfuy498u31br89341&*#Y$*@#oihfweo",
        "role": "Doctor",
        "is_active": True,
        "username": "JaneDoe",
        "is_first": False,
        "created_at": "2023-10-01T12:00:00Z"
      },
    ]
  
  def createUser(self, user: User):
    try:
      # Simulate creating a user
      new_user = {
        "id": len(self.users) + 1,
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "role": user.role.value,
        "username": user.username,
        "is_active": True,
        "is_first": True,
        "created_at": "2023-10-01T12:00:00Z",
      }
      print(new_user)
      self.users.append(new_user)
      return True
    except Exception as e:
      raise Exception(f"Erro ao Criar Usuário: {e}")