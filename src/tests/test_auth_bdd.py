from pytest_bdd import scenario, given, when, then, parsers
from src.services.auth_service import AuthService
from src.services.user_service import UserServices
from src.mock.user_repository_mock import UserRepositoryMock
from src.schemas.user_schema import LoginUserRequest, ChangePasswordRequest
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

# ==========================================
# Alteração de senha
# ==========================================

@scenario(feature_file, 'Alteração de senha')
def test_change_password():
    pass

@given('quero alterar minha senha')
def want_to_change_password():
    pass

@when(parsers.parse('eu altero minha senha para "{new_password}"'))
def change_password(new_password):
    global token, login_data
    change_password_request = ChangePasswordRequest(
        identifier=login_data['identifier'],
        new_password=new_password
    )
    user_service = UserServices(repo)
    message = user_service.changePassword(
        identifier=change_password_request.identifier,
        new_password=change_password_request.new_password
    )
    assert message is None

@then('a senha deve ser alterada com sucesso')
def verify_password_changed():
    # Tentamos fazer login com a nova senha para verificar
    login_request = LoginUserRequest(
        identifier=login_data['identifier'],
        password="senha456"
    )
    new_token = auth_service.login(
        identifier=login_request.identifier,
        password=login_request.password
    )
    assert new_token is not None 