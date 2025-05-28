from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.entities.schedule_tag import ScheduleTagEntity
from src.repositories.schedule_tag_repository import ScheduleTagRepository
from src.schemas.schedule_tag_schema import ScheduleTagCreateRequest

class ScheduleTagService:
    def __init__(self, repo: ScheduleTagRepository):
        self.repo = repo

    def create_schedule_tag(self, request: ScheduleTagCreateRequest) -> ScheduleTagEntity:
        try:
            if not request.name or not request.description:
                raise HTTPException(status_code=422, detail="Todos os campos são obrigatórios")
            
            new_schedule_tag = ScheduleTagEntity(
                name=request.name,
                description=request.description
            )
            
            created_tag = self.repo.create_schedule_tag(new_schedule_tag)
            if not created_tag or not created_tag.schedule_tag_id:
                raise HTTPException(status_code=500, detail="Erro ao criar tag de agendamento")
                
            return created_tag
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar tag de agendamento: {str(e)}")

    