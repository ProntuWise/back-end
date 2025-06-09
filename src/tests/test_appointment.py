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