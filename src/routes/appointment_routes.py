import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.schemas.appointment_schema import AppointmentCreateRequest, AppointmentUpdateRequest
from src.services.appointment_service import AppointmentService
from src.utils.helpers import handle_database_exception


dev_mode = os.getenv("DEV_MODE")
router = APIRouter(
    prefix="/appointment",
    tags=["appointments"]
)

@router.post("", response_model=AppointmentCreateRequest)
async def create_appointment(appointment: AppointmentCreateRequest):
    try:
        # Validação dos campos obrigatórios
        if not appointment.date or not appointment.time or not appointment.duration:
            return JSONResponse(status_code=422, content={"message": "Data, hora e duração são campos obrigatórios"})
        
        if not appointment.patient_id or not appointment.user_id:
            return JSONResponse(status_code=422, content={"message": "ID do paciente e do usuário são obrigatórios"})
        
        # Inicialização do repositório baseado no modo
        if dev_mode == "True":
            from src.repositories.appointment_repository import AppointmentRepository
            repo = AppointmentRepository()
        else:
            from src.mock.appointment_repository_mock import AppointmentRepositoryMock
            repo = AppointmentRepositoryMock()
        
        # Criação do agendamento
        created_appointment = AppointmentService(repo).create_appointment(appointment)
        
        if not created_appointment:
            return JSONResponse(status_code=400, content={"message": "Erro ao criar agendamento"})
    
        return JSONResponse(
            status_code=201, 
            content={
                "message": "Agendamento criado com sucesso!",
            }
        )
    except Exception as e:
        return handle_database_exception(e, "CreateAppointment")

@router.get("")
async def get_all_appointments():
    try:
        if dev_mode == "True":
            from src.repositories.appointment_repository import AppointmentRepository
            repo = AppointmentRepository()
        else:
            from src.mock.appointment_repository_mock import AppointmentRepositoryMock
            repo = AppointmentRepositoryMock()
        
        appointments = AppointmentService(repo).get_appointments()
        return JSONResponse(
            status_code=200,
            content={
                "message": "Agendamentos buscados com sucesso!",
                "appointments": appointments
            }
        )
    except Exception as e:
        return handle_database_exception(e, "GetAllAppointments")

@router.put("/{appointment_id}")
async def update_appointment(appointment_id: int, appointment: AppointmentUpdateRequest):
    try:
        if dev_mode == "True":
            from src.repositories.appointment_repository import AppointmentRepository
            repo = AppointmentRepository()
        else:
            from src.mock.appointment_repository_mock import AppointmentRepositoryMock
            repo = AppointmentRepositoryMock()
        
        AppointmentService(repo).update_appointment(appointment_id, appointment)
        
        return JSONResponse(
            status_code=200,
            content={
                "message": "Agendamento atualizado com sucesso!",
            }
        )
    except Exception as e:
        return handle_database_exception(e, "UpdateAppointment")

@router.delete("/{appointment_id}")
async def delete_appointment(appointment_id: int):
    try:
        if dev_mode == "True":
            from src.repositories.appointment_repository import AppointmentRepository
            repo = AppointmentRepository()
        else:
            from src.mock.appointment_repository_mock import AppointmentRepositoryMock
            repo = AppointmentRepositoryMock()
        
        AppointmentService(repo).delete_appointment(appointment_id)
        
        return JSONResponse(
            status_code=200,
            content={
                "message": "Agendamento deletado com sucesso!",
            }
        )
    except Exception as e:
        return handle_database_exception(e, "DeleteAppointment")
