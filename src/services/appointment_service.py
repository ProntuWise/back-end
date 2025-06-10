from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.entities.appointment import AppointmentEntity
from src.repositories.appointment_repository import AppointmentRepository
from src.schemas.appointment_schema import AppointmentCreateRequest

class AppointmentService:
    def __init__(self, repo: AppointmentRepository):
        self.repo = repo

    def create_appointment(self, request: AppointmentCreateRequest) -> AppointmentEntity:
        try:
            # Validação dos campos obrigatórios
            if not request.date or not request.time or not request.duration:
                raise HTTPException(status_code=422, detail="Data, hora e duração são campos obrigatórios")
            
            if not request.patient_id or not request.user_id:
                raise HTTPException(status_code=422, detail="ID do paciente e do usuário são obrigatórios")
            
            # Criação da entidade
            new_appointment = AppointmentEntity(
                date=request.date,
                time=request.time,
                duration=request.duration,
                patient_id=request.patient_id,
                user_id=request.user_id,
                tag_id=request.tag_id,
                description=request.description,
                status=request.status,
                appointment_type=request.appointment_type
            )
            
            # Criação no repositório
            created_appointment = self.repo.create_appointment(new_appointment)
            if not created_appointment or not created_appointment.appointment_id:
                raise HTTPException(status_code=500, detail="Erro ao criar agendamento")
                
            return created_appointment
            
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar agendamento: {str(e)}")

    def get_appointments(self):
        try:
            appointments = self.repo.get_appointments()
            return appointments
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar agendamentos: {str(e)}")
    