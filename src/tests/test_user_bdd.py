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

# ==========================================
# Deletar um usuário existente
# ==========================================

@scenario(feature_file, 'Deletar um usuário existente')
def test_delete_user():
    pass

@given(parsers.parse('existe um usuário com ID {user_id:d}'))
def user_exists(user_id):
    global user_data, user, repo, user_service
    # Criamos um usuário primeiro para garantir que existe
    repo = UserRepositoryMock()
    user_service = UserServices(repo)
    user_data = {
        'name': "Isaias Cano Bello da Luz",
        'email': "isaias@gmail.com",
        'password': "ajdbhfuy498u31br89341&*#Y$*@#oihfweo",
        'role': UserTypeEnum.Doctor
    }
    user = User(**user_data)
    user.user_id = user_id
    repo.createUser(user)
    
@when('eu deletar o usuário')
def delete_user():
    global user, repo, user_service
    message = user_service.deleteUser(user.user_id)
    assert message is None

@then('o usuário deve ser removido com sucesso')
def verify_user_deleted():
    global repo, user
    # Tentar buscar o usuário deve retornar None
    deleted_user = repo.getUserById(user.user_id)
    assert deleted_user is None