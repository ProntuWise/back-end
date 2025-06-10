from pytest_bdd import scenario, given, when, then, parsers
from src.services.user_service import UserServices
from src.mock.user_repository_mock import UserRepositoryMock
from src.enums.user_type_enum import UserTypeEnum
from src.entities.user import User
import os

user_data = {}
user = None

current_dir = os.path.dirname(os.path.abspath(__file__))
feature_file = os.path.join(current_dir, 'features', 'user.feature')

@scenario(feature_file, 'Cadastrar um novo usuário médico')
def test_create_user():
    pass

@given('que sou um administrador do sistema')
def setup_admin():
    global repo, user_service
    repo = UserRepositoryMock()
    user_service = UserServices(repo)

@given('tenho os dados do novo usuário')
def setup_user_data():
    global user_data
    user_data = {}

@given(parsers.parse('o nome é "{name}"'))
def set_name(name):
    global user_data
    user_data['name'] = name

@given(parsers.parse('o email é "{email}"'))
def set_email(email):
    global user_data
    user_data['email'] = email

@given(parsers.parse('a senha é "{password}"'))
def set_password(password):
    global user_data
    user_data['password'] = password

@given(parsers.parse('o tipo de usuário é "{role}"'))
def set_role(role):
    global user_data
    user_data['role'] = UserTypeEnum(role)

@when('eu cadastrar o usuário')
def create_user():
    global user, user_data
    user_entity = User(**user_data)
    user = user_service.createUser(user_entity)

@then('o usuário deve ser cadastrado com sucesso')
def verify_user_created():
    assert user is not None

@then('os dados do usuário devem estar corretos')
def verify_user_data():
    assert user.name == user_data['name']
    assert user.email == user_data['email']
    assert user.role.value == user_data['role'].value
    assert user.password is not None