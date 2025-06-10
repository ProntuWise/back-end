from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from typing import List

from src.utils.helpers import handle_database_exception
from src.services.doctor_services import DoctorServices

router = APIRouter(
  prefix="/doctorAI",
  tags=["doctor"]
)

@router.post("")
async def analyzePatientData(files: List[UploadFile] = File(...)):
    try:
        # Instancia o serviço e processa os arquivos
        doctor_service = DoctorServices()
        result = await doctor_service.analyzePatientData(files)
        
        return JSONResponse(
            content=result,
            status_code=200
        )
    except Exception as e:
        return handle_database_exception(e)
