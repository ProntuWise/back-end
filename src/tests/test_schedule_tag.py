def test_create_schedule_tag():
    from src.services.schedule_tag_service import ScheduleTagService
    from src.mock.schedule_tag_repository_mock import ScheduleTagRepositoryMock
    from src.schemas.schedule_tag_schema import ScheduleTagCreateRequest

    # Mock the repository
    repo = ScheduleTagRepositoryMock()
    schedule_tag_service = ScheduleTagService(repo)

    # Create test data
    tag_data = ScheduleTagCreateRequest(
        name="Consulta Pediátrica",
        description="Agendamento para consultas pediátricas"
    )

    # Create schedule tag
    tag = schedule_tag_service.create_schedule_tag(tag_data)

    # Assertions
    assert tag is not None
    assert tag.schedule_tag_id == 3  # Since we have 2 initial tags in the mock
    assert tag.name == "Consulta Pediátrica"
    assert tag.description == "Agendamento para consultas pediátricas" 