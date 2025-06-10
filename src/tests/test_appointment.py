def test_create_appointment():
    from src.services.appointment_service import AppointmentService
    from src.mock.appointment_repository_mock import AppointmentRepositoryMock
    from src.entities.appointment import AppointmentEntity
    from src.enums.appointment_status_enum import AppointmentStatusEnum
    from src.enums.appointment_type_enum import AppointmentTypeEnum
    from datetime import date, time
    from src.schemas.appointment_schema import AppointmentCreateRequest

    # Mock the repository
    repo = AppointmentRepositoryMock()
    appointment_service = AppointmentService(repo)

    # Create test data
    appointment_data = AppointmentCreateRequest(
        date=date(2024, 3, 20),
        time=time(14, 30),
        duration=30,
        patient_id=1,
        user_id=1,
        tag_id=1,
        description="Consulta de rotina",
        status="Confirmed",
        appointment_type="First_Visit"
    )

    # Create appointment
    appointment = appointment_service.create_appointment(appointment_data)

    # Assertions
    assert appointment is not None
    assert appointment.appointment_id == 1
    assert appointment.date == date(2024, 3, 20)
    assert appointment.time == time(14, 30)
    assert appointment.duration == 30
    assert appointment.patient_id == 1
    assert appointment.user_id == 1
    assert appointment.tag_id == 1
    assert appointment.description == "Consulta de rotina"
    assert appointment.status == "Confirmed"
    assert appointment.appointment_type == "First_Visit" 

def test_get_all_appointments():
    from src.services.appointment_service import AppointmentService
    from src.mock.appointment_repository_mock import AppointmentRepositoryMock
    from src.entities.appointment import AppointmentEntity
    from src.enums.appointment_status_enum import AppointmentStatusEnum
    from src.enums.appointment_type_enum import AppointmentTypeEnum
    from datetime import date, time
    from src.schemas.appointment_schema import AppointmentCreateRequest
    
    # Mock the repository
    repo = AppointmentRepositoryMock()
    appointment_service = AppointmentService(repo)

    # Create test data
    appointment_data = AppointmentCreateRequest(
        date=date(2024, 3, 20),
        time=time(14, 30),
        duration=30,
        patient_id=1,
        user_id=1,
        tag_id=1,
        description="Consulta de rotina",
        status="Confirmed",
        appointment_type="First_Visit"
    )
    # Create appointment
    appointment = appointment_service.create_appointment(appointment_data)

    # Get all appointments
    appointments = appointment_service.get_appointments()

    # Assertions
    assert appointments is not None
    assert len(appointments) == 1
    assert appointments[0].appointment_id == appointment.appointment_id
    assert str(appointments[0].date) == str(appointment.date)

def test_update_appointment():
    from src.services.appointment_service import AppointmentService
    from src.mock.appointment_repository_mock import AppointmentRepositoryMock
    from datetime import date, time
    from src.schemas.appointment_schema import AppointmentCreateRequest, AppointmentUpdateRequest

    # Mock the repository
    repo = AppointmentRepositoryMock()
    appointment_service = AppointmentService(repo)

    # Create test data
    appointment_data = AppointmentCreateRequest(
        date=date(2024, 3, 20),
        time=time(14, 30),
        duration=30,
        patient_id=1,
        user_id=1,
        tag_id=1,
        description="Consulta de rotina",
        status="Confirmed",
        appointment_type="First_Visit"
    )

    # Create appointment
    appointment = appointment_service.create_appointment(appointment_data)

    # Update appointment
    update_data = AppointmentUpdateRequest(
        date="2024-03-21",
        time="15:30:00",
        duration=45,
        patient_id=2,
        user_id=2,
        tag_id=2,
        description="Consulta de rotina atualizada",
        status="Confirmed",
        appointment_type="First_Visit"
    )

    updated_appointment = appointment_service.update_appointment(appointment.appointment_id, update_data)

    # Assertions
    assert updated_appointment is not None
    assert updated_appointment.appointment_id == appointment.appointment_id
    assert updated_appointment.date == date(2024, 3, 21)
    assert updated_appointment.time == time(15, 30)
    assert updated_appointment.duration == 45
    assert updated_appointment.patient_id == 2
    assert updated_appointment.user_id == 2

def test_delete_appointment():
    from src.services.appointment_service import AppointmentService
    from src.mock.appointment_repository_mock import AppointmentRepositoryMock
    from src.entities.appointment import AppointmentEntity
    from src.enums.appointment_status_enum import AppointmentStatusEnum
    from src.enums.appointment_type_enum import AppointmentTypeEnum
    from datetime import date, time
    from src.schemas.appointment_schema import AppointmentCreateRequest
    
    # Mock the repository
    repo = AppointmentRepositoryMock()
    appointment_service = AppointmentService(repo)

    # Create test data
    appointment_data = AppointmentCreateRequest(
        date=date(2024, 3, 20),
        time=time(14, 30),
        duration=30,
        patient_id=1,
        user_id=1,
        tag_id=1,
        description="Consulta de rotina",
        status="Confirmed",
        appointment_type="First_Visit"
    )

    # Create appointment
    appointment = appointment_service.create_appointment(appointment_data)

    # Delete appointment
    deleted_appointment = appointment_service.delete_appointment(appointment.appointment_id)

    # Assertions
    assert deleted_appointment is not None
    assert deleted_appointment.appointment_id == appointment.appointment_id
    assert deleted_appointment.date == date(2024, 3, 20)
    assert deleted_appointment.time == time(14, 30)
