import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.schemas.patient_schema import PatientCreateRequest
from src.services.patient_service import PatientService
from src.utils.helpers import handle_database_exception


dev_mode = os.getenv("DEV_MODE")
router = APIRouter(
  prefix="/patient",
  tags=["patients"]
)

@router.post("/create-patient", response_model=PatientCreateRequest)
async def create_patient(patient: PatientCreateRequest):
    try:
        if not patient.name or not patient.cpf:
            return JSONResponse(status_code=422, content={"message": "Nome e CPF são campos obrigatórios"})
        
        if dev_mode == "True":
            from src.repositories.patient_repository import PatientRepository
            repo = PatientRepository()
        else:
            from src.mock.patient_repository_mock import PatientRepositoryMock
            repo = PatientRepositoryMock()
        
        created_patient = PatientService(repo).create_patient(patient)
        
        if not created_patient:
            return JSONResponse(status_code=400, content={"message": "Erro ao criar paciente"})
    
        return JSONResponse(
            status_code=201, 
            content={
                "message": "Paciente criado com sucesso!",
            }
        )
    except Exception as e:
        return handle_database_exception(e, "CreatePatient") 