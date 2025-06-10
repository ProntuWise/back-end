from pytest_bdd import scenario, given, when, then, parsers
from src.services.auth_service import AuthService
from src.mock.user_repository_mock import UserRepositoryMock
from src.schemas.user_schema import LoginUserRequest
import os

login_data = {}
token = None

current_dir = os.path.dirname(os.path.abspath(__file__))
feature_file = os.path.join(current_dir, 'features', 'auth.feature')

@scenario(feature_file, 'Login com credenciais válidas')
def test_login():
    pass

@given('que sou um usuário cadastrado no sistema')
def setup_auth():
    global repo, auth_service
    repo = UserRepositoryMock()
    auth_service = AuthService(repo)

@given(parsers.parse('meu email é "{email}"'))
def set_email(email):
    global login_data
    login_data['identifier'] = email

@given(parsers.parse('minha senha é "{password}"'))
def set_password(password):
    global login_data
    login_data['password'] = password

@when('eu tento fazer login')
def do_login():
    global token, login_data
    login_request = LoginUserRequest(**login_data)
    token = auth_service.login(
        identifier=login_request.identifier,
        password=login_request.password
    )

@then('o login deve ser bem-sucedido')
def verify_login_success():
    assert token is not None

@then('devo receber um token de autenticação válido')
def verify_token():
    assert isinstance(token, str) 