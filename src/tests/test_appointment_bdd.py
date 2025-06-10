from pytest_bdd import scenario, given, when, then, parsers
from src.services.appointment_service import AppointmentService
from src.mock.appointment_repository_mock import AppointmentRepositoryMock
from src.schemas.appointment_schema import AppointmentCreateRequest
from datetime import datetime, date, time
import os

appointment_data = {}
appointment = None

current_dir = os.path.dirname(os.path.abspath(__file__))
feature_file = os.path.join(current_dir, 'features', 'appointment.feature')

@scenario(feature_file, 'Criar uma nova consulta')
def test_create_appointment():
    pass

@given('que sou um profissional da clínica')
def setup_professional():
    global repo, appointment_service
    repo = AppointmentRepositoryMock()
    appointment_service = AppointmentService(repo)

@given('tenho os dados necessários para agendar uma consulta')
def setup_appointment_data():
    global appointment_data
    appointment_data = {}

@given(parsers.parse('a data escolhida é "{date_str}"'))
def set_date(date_str):
    global appointment_data
    appointment_data['date'] = datetime.strptime(date_str, '%Y-%m-%d').date()

@given(parsers.parse('o horário escolhido é "{time_str}"'))
def set_time(time_str):
    global appointment_data
    appointment_data['time'] = datetime.strptime(time_str, '%H:%M').time()

@given(parsers.parse('a duração será de {duration:d} minutos'))
def set_duration(duration):
    global appointment_data
    appointment_data['duration'] = duration

@given(parsers.parse('o ID do paciente é {patient_id:d}'))
def set_patient_id(patient_id):
    global appointment_data
    appointment_data['patient_id'] = patient_id

@given(parsers.parse('o ID do profissional é {user_id:d}'))
def set_user_id(user_id):
    global appointment_data
    appointment_data['user_id'] = user_id

@given(parsers.parse('o ID da tag é {tag_id:d}'))
def set_tag_id(tag_id):
    global appointment_data
    appointment_data['tag_id'] = tag_id

@given(parsers.parse('a descrição é "{description}"'))
def set_description(description):
    global appointment_data
    appointment_data['description'] = description

@given(parsers.parse('o status é "{status}"'))
def set_status(status):
    global appointment_data
    appointment_data['status'] = status

@given(parsers.parse('o tipo de consulta é "{appointment_type}"'))
def set_appointment_type(appointment_type):
    global appointment_data
    appointment_data['appointment_type'] = appointment_type

@when('eu criar a consulta')
def create_appointment():
    global appointment, appointment_data
    request = AppointmentCreateRequest(**appointment_data)
    appointment = appointment_service.create_appointment(request)

@then('a consulta deve ser criada com sucesso')
def verify_appointment_created():
    assert appointment is not None
    assert appointment.appointment_id == 1

@then('os dados da consulta devem estar corretos')
def verify_appointment_data():
    assert appointment.date == appointment_data['date']
    assert appointment.time == appointment_data['time']
    assert appointment.duration == appointment_data['duration']
    assert appointment.patient_id == appointment_data['patient_id']
    assert appointment.user_id == appointment_data['user_id']
    assert appointment.tag_id == appointment_data['tag_id']
    assert appointment.description == appointment_data['description']
    assert appointment.status == appointment_data['status']
    assert appointment.appointment_type == appointment_data['appointment_type'] 