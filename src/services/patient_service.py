from fastapi import HTTPException
from src.entities.patient import PatientEntity
from src.repositories.patient_repository import PatientRepository
from src.schemas.patient_schema import PatientCreateRequest

class PatientService:
    def __init__(self, repo: PatientRepository):
        self.repo = repo

    def create_patient(self, request: PatientCreateRequest) -> PatientEntity:
        try:
            if not request.name or not request.cpf:
                raise HTTPException(status_code=422, detail="Nome e CPF são campos obrigatórios")
            
            new_patient = PatientEntity(
                name=request.name,
                cpf=request.cpf,
                rg=request.rg,
                birth_date=request.birth_date,
                phone=request.phone,
                email=request.email,
                address=request.address,
                gender=request.gender,
                folder_path=request.folder_path
            )
            
            if request.email:
                try:
                    new_patient.validateEmail(request.email)
                except ValueError as e:
                    raise HTTPException(status_code=422, detail=str(e))
            
            created_patient = self.repo.create_patient(new_patient)
            if not created_patient or not created_patient.patient_id:
                raise HTTPException(status_code=500, detail="Erro ao criar paciente")
                
            return created_patient
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar paciente: {str(e)}")
