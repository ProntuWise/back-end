import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.schemas.schedule_tag_schema import ScheduleTagCreateRequest
from src.services.schedule_tag_service import ScheduleTagService
from src.utils.helpers import handle_database_exception


dev_mode = os.getenv("DEV_MODE")
router = APIRouter(
    tags=["schedule_tags"]
)

@router.post("/create-schedule-tag", response_model=ScheduleTagCreateRequest)
async def create_schedule_tag(schedule_tag: ScheduleTagCreateRequest):
    try:
        if not schedule_tag.name or not schedule_tag.description:
            return JSONResponse(status_code=422, content={"message": "Todos os campos são obrigatórios"})
        
        if dev_mode == True:
            from src.repositories.schedule_tag_repository import ScheduleTagRepository
            repo = ScheduleTagRepository()
        else:
            from src.mock.schedule_tag_repository_mock import ScheduleTagRepositoryMock
            repo = ScheduleTagRepositoryMock()
        
        schedule_tag = ScheduleTagService(repo).create_schedule_tag(schedule_tag)
        
        if not schedule_tag:
            return JSONResponse(status_code=400, content={"message": "Erro ao criar tag de agendamento"})
    
        return JSONResponse(
            status_code=201, 
            content={
                "message": "Tag de agendamento criada com sucesso!"
            }
        )
    except Exception as e:
        return handle_database_exception(e, "CreateScheduleTag")