from pytest_bdd import scenario, given, when, then, parsers
from src.services.patient_service import PatientService
from src.mock.patient_repository_mock import PatientRepositoryMock
from src.schemas.patient_schema import PatientCreateRequest
from datetime import datetime
import os

patient_data = {}
patient = None

current_dir = os.path.dirname(os.path.abspath(__file__))
feature_file = os.path.join(current_dir, 'features', 'patient.feature')

@scenario(feature_file, 'Cadastrar um novo paciente')
def test_create_patient():
    pass

@given('que sou um profissional da clínica')
def setup_professional():
    global repo, patient_service
    repo = PatientRepositoryMock()
    patient_service = PatientService(repo)

@given('tenho os dados do paciente para cadastro')
def setup_patient_data():
    global patient_data
    patient_data = {}

@given(parsers.parse('o nome do paciente é "{name}"'))
def set_name(name):
    global patient_data
    patient_data['name'] = name

@given(parsers.parse('o CPF é "{cpf}"'))
def set_cpf(cpf):
    global patient_data
    patient_data['cpf'] = cpf

@given(parsers.parse('o RG é "{rg}"'))
def set_rg(rg):
    global patient_data
    patient_data['rg'] = rg

@given(parsers.parse('a data de nascimento é "{birth_date}"'))
def set_birth_date(birth_date):
    global patient_data
    patient_data['birth_date'] = datetime.strptime(birth_date, '%Y-%m-%d').date()

@given(parsers.parse('o telefone é "{phone}"'))
def set_phone(phone):
    global patient_data
    patient_data['phone'] = phone

@given(parsers.parse('o email é "{email}"'))
def set_email(email):
    global patient_data
    patient_data['email'] = email

@given(parsers.parse('o endereço é "{address}"'))
def set_address(address):
    global patient_data
    patient_data['address'] = address

@given(parsers.parse('o gênero é "{gender}"'))
def set_gender(gender):
    global patient_data
    patient_data['gender'] = gender

@given(parsers.parse('o caminho da pasta é "{folder_path}"'))
def set_folder_path(folder_path):
    global patient_data
    patient_data['folder_path'] = folder_path

@when('eu cadastrar o paciente')
def create_patient():
    global patient, patient_data
    request = PatientCreateRequest(**patient_data)
    patient = patient_service.create_patient(request)

@then('o paciente deve ser cadastrado com sucesso')
def verify_patient_created():
    assert patient is not None

@then('deve ter um ID único')
def verify_patient_id():
    assert patient.patient_id == 1

@then('os dados do paciente devem estar corretos')
def verify_patient_data():
    assert patient.name == patient_data['name']
    assert patient.cpf == patient_data['cpf']
    assert patient.rg == patient_data['rg']
    assert patient.birth_date == patient_data['birth_date']
    assert patient.phone == patient_data['phone']
    assert patient.email == patient_data['email']
    assert patient.address == patient_data['address']
    assert patient.gender == patient_data['gender']
    assert patient.folder_path == patient_data['folder_path'] 