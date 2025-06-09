def test_create_patient():
    from src.services.patient_service import PatientService
    from src.mock.patient_repository_mock import PatientRepositoryMock
    from src.schemas.patient_schema import PatientCreateRequest
    from src.enums.gender_enum import GenderEnum
    from datetime import date

    # Mock the repository
    repo = PatientRepositoryMock()
    patient_service = PatientService(repo)

    # Create test data
    patient_data = PatientCreateRequest(
        name="Maria Silva",
        cpf="123.456.789-00",
        rg="12.345.678-9",
        birth_date=date(1990, 5, 15),
        phone="(11) 98765-4321",
        email="maria.silva@email.com",
        address="Rua das Flores, 123",
        gender="Female",
        folder_path="/pacientes/maria_silva"
    )

    # Create patient
    patient = patient_service.create_patient(patient_data)

    # Assertions
    assert patient is not None
    assert patient.patient_id == 1
    assert patient.name == "Maria Silva"
    assert patient.cpf == "123.456.789-00"
    assert patient.rg == "12.345.678-9"
    assert patient.birth_date == date(1990, 5, 15)
    assert patient.phone == "(11) 98765-4321"
    assert patient.email == "maria.silva@email.com"
    assert patient.address == "Rua das Flores, 123"
    assert patient.gender == "Female"
    assert patient.folder_path == "/pacientes/maria_silva" 