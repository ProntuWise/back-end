def test_login_user():
  from src.services.auth_service import AuthService
  from src.mock.user_repository_mock import UserRepositoryMock
  from src.entities.user import LoginUserRequest

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