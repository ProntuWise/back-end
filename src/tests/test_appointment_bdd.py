from pytest_bdd import scenario, given, when, then, parsers
from src.services.appointment_service import AppointmentService
from src.mock.appointment_repository_mock import AppointmentRepositoryMock
from src.schemas.appointment_schema import AppointmentCreateRequest, AppointmentUpdateRequest
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

# ==========================================
# Listar todas as consultas
# ==========================================

@scenario(feature_file, 'Listar todas as consultas')
def test_list_appointments():
    pass

@given('existe pelo menos uma consulta cadastrada')
def appointment_exists():
    global appointment_data, appointment, repo, appointment_service
    # Criamos uma consulta primeiro para garantir que existe
    repo = AppointmentRepositoryMock()
    appointment_service = AppointmentService(repo)
    
    appointment_data = {
        'date': date(2024, 3, 20),
        'time': time(14, 30),
        'duration': 30,
        'patient_id': 1,
        'user_id': 1,
        'tag_id': 1,
        'description': "Consulta de rotina",
        'status': "Confirmed",
        'appointment_type': "First_Visit"
    }
    
    appointment_request = AppointmentCreateRequest(**appointment_data)
    appointment = appointment_service.create_appointment(appointment_request)

@when('eu solicitar a lista de consultas')
def list_appointments():
    global appointments, repo, appointment_service
    appointments = appointment_service.get_appointments()

@then('devo receber uma lista não vazia de consultas')
def verify_appointments_list():
    assert appointments is not None
    assert len(appointments) > 0

@then('os dados das consultas devem estar corretos')
def verify_appointments_data():
    # Verificamos o primeiro appointment que criamos
    first_appointment = appointments[0]
    assert first_appointment.appointment_id == appointment.appointment_id
    assert str(first_appointment.date) == str(appointment_data['date'])
    assert str(first_appointment.time) == str(appointment_data['time'])
    assert first_appointment.duration == appointment_data['duration']
    assert first_appointment.patient_id == appointment_data['patient_id']
    assert first_appointment.user_id == appointment_data['user_id']
    assert first_appointment.tag_id == appointment_data['tag_id']
    assert first_appointment.description == appointment_data['description']
    assert first_appointment.status == appointment_data['status']
    assert first_appointment.appointment_type == appointment_data['appointment_type']

# ==========================================
# Atualizar uma consulta
# ==========================================

@scenario(feature_file, 'Atualizar uma consulta existente')
def test_update_appointment():
    pass

@given('existe uma consulta cadastrada')
def existing_appointment():
    global appointment_data, appointment, repo, appointment_service
    # Criamos uma consulta primeiro para garantir que existe
    repo = AppointmentRepositoryMock()
    appointment_service = AppointmentService(repo)
    
    appointment_data = {
        'date': date(2024, 3, 20),
        'time': time(14, 30),
        'duration': 30,
        'patient_id': 1,
        'user_id': 1,
        'tag_id': 1,
        'description': "Consulta de rotina",
        'status': "Scheduled",
        'appointment_type': "First_Visit"
    }
    
    appointment_request = AppointmentCreateRequest(**appointment_data)
    appointment = appointment_service.create_appointment(appointment_request)

@given('quero atualizar os dados da consulta')
def setup_update_data():
    global update_data
    update_data = {}

@given(parsers.parse('a nova data é "{date_str}"'))
def set_new_date(date_str):
    global update_data
    update_data['date'] = datetime.strptime(date_str, '%Y-%m-%d').date()

@given(parsers.parse('o novo horário é "{time_str}"'))
def set_new_time(time_str):
    global update_data
    update_data['time'] = datetime.strptime(time_str, '%H:%M').time()

@given(parsers.parse('a nova duração será de {duration:d} minutos'))
def set_new_duration(duration):
    global update_data
    update_data['duration'] = duration

@given(parsers.parse('a nova descrição é "{description}"'))
def set_new_description(description):
    global update_data
    update_data['description'] = description

@given(parsers.parse('o novo status é "{status}"'))
def set_new_status(status):
    global update_data
    update_data['status'] = status

@when('eu atualizar a consulta')
def update_appointment():
    global updated_appointment, update_data, appointment
    # Mantemos os IDs originais
    update_data['patient_id'] = appointment.patient_id
    update_data['user_id'] = appointment.user_id
    update_data['tag_id'] = appointment.tag_id
    update_data['appointment_type'] = appointment.appointment_type
    
    # Convertemos a data e hora para strings ISO format
    update_data['date'] = update_data['date'].isoformat()
    update_data['time'] = update_data['time'].isoformat()
    
    updated_appointment = appointment_service.update_appointment(appointment.appointment_id, AppointmentUpdateRequest(**update_data))

@then('a consulta deve ser atualizada com sucesso')
def verify_appointment_updated():
    assert updated_appointment is not None
    assert updated_appointment.appointment_id == appointment.appointment_id

@then('os novos dados da consulta devem estar corretos')
def verify_updated_data():
    assert str(updated_appointment.date) == str(update_data['date'])
    assert str(updated_appointment.time) == str(update_data['time'])
    assert updated_appointment.duration == update_data['duration']
    assert updated_appointment.description == update_data['description']
    assert updated_appointment.status.value == update_data['status']
    # Verificamos que os IDs permanecem os mesmos
    assert updated_appointment.patient_id == appointment.patient_id
    assert updated_appointment.user_id == appointment.user_id
    assert updated_appointment.tag_id == appointment.tag_id
    assert updated_appointment.appointment_type == appointment.appointment_type

# ==========================================
# Excluir uma consulta
# ==========================================

@scenario(feature_file, 'Excluir uma consulta')
def test_delete_appointment():
    pass

@when('eu excluir a consulta')
def delete_appointment():
    global appointment
    appointment_service.delete_appointment(appointment.appointment_id)

@then('a consulta deve ser excluída com sucesso')
def verify_appointment_deleted():
    # A exclusão não deve lançar exceções
    pass

@then('a consulta não deve mais existir no sistema')
def verify_appointment_not_exists():
    appointments = appointment_service.get_appointments()
    appointment_ids = [app.appointment_id for app in appointments]
    assert appointment.appointment_id not in appointment_ids 
