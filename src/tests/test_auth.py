def test_login_user():
  from src.services.auth_service import AuthService
  from src.mock.user_repository_mock import UserRepositoryMock
  from src.schemas.user_schema import LoginUserRequest

  # Mock the repository
  repo = UserRepositoryMock()
  auth_service = AuthService(repo)

  # Create a mock login request
  login_request = LoginUserRequest(
      identifier="John@gmail.com",
      password="senha123"
  )

  # Call the login method
  token = auth_service.login(
      identifier=login_request.identifier,
      password=login_request.password
  )

  assert token is not None
  assert isinstance(token, str)

def test_change_password():
  from src.services.user_service import UserServices
  from src.mock.user_repository_mock import UserRepositoryMock
  from src.schemas.user_schema import ChangePasswordRequest

  # Mock the repository
  repo = UserRepositoryMock()
  user_service = UserServices(repo)

  # Create a mock change password request
  change_password_request = ChangePasswordRequest(
    identifier="John@gmail.com",
    new_password="senha123",
  )

  # Call the change password method
  message = user_service.changePassword(
    identifier=change_password_request.identifier,
    new_password="senha456"
  )

  assert message is None
