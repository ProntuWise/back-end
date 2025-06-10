from pytest_bdd import scenario, given, when, then, parsers
from src.services.schedule_tag_service import ScheduleTagService
from src.mock.schedule_tag_repository_mock import ScheduleTagRepositoryMock
from src.schemas.schedule_tag_schema import ScheduleTagCreateRequest
import os

tag_data = {}
tag = None

current_dir = os.path.dirname(os.path.abspath(__file__))
feature_file = os.path.join(current_dir, 'features', 'schedule_tag.feature')

@scenario(feature_file, 'Criar uma nova tag de agendamento')
def test_create_schedule_tag():
    pass

@given('que sou um administrador da clínica')
def setup_admin():
    global repo, schedule_tag_service
    repo = ScheduleTagRepositoryMock()
    schedule_tag_service = ScheduleTagService(repo)

@given('quero criar uma nova categoria de agendamento')
def setup_tag_data():
    global tag_data
    tag_data = {}

@given(parsers.parse('o nome da tag é "{name}"'))
def set_name(name):
    global tag_data
    tag_data['name'] = name

@given(parsers.parse('a descrição da tag é "{description}"'))
def set_description(description):
    global tag_data
    tag_data['description'] = description

@when('eu criar a tag de agendamento')
def create_tag():
    global tag, tag_data
    request = ScheduleTagCreateRequest(**tag_data)
    tag = schedule_tag_service.create_schedule_tag(request)

@then('a tag deve ser criada com sucesso')
def verify_tag_created():
    assert tag is not None

@then('deve ter um ID único')
def verify_tag_id():
    assert tag.schedule_tag_id == 3  # Considerando os 2 registros iniciais do mock

@then('os dados da tag devem estar corretos')
def verify_tag_data():
    assert tag.name == tag_data['name']
    assert tag.description == tag_data['description'] 