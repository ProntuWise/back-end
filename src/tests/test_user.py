def test_create_user():
  from src.services.user_service import UserServices
  from src.mock.user_repository_mock import UserRepositoryMock
  from src.enums.user_type_enum import UserTypeEnum
  from src.entities.user import User

  # Mock the repository
  repo = UserRepositoryMock()
  user_service = UserServices(repo)
  user_data = User(
    name="Isaias Cano Bello da Luz",
    email="isaias@gmail.com",
    password="ajdbhfuy498u31br89341&*#Y$*@#oihfweo",
    role=UserTypeEnum.Doctor,
  )
  user = user_service.createUser(user_data)

  assert user is not None
  assert user.name == "Isaias Cano Bello da Luz"
  assert user.email == "isaias@gmail.com"
  assert user.role.value == "Doctor"
  assert user.password is not None

def test_delete_user():
  from src.services.user_service import UserServices
  from src.mock.user_repository_mock import UserRepositoryMock
  from src.entities.user import User
  from src.enums.user_type_enum import UserTypeEnum
  from datetime import datetime

  # Mock the repository
  repo = UserRepositoryMock()
  user_service = UserServices(repo)

  message = user_service.deleteUser(1)

  assert message is None
