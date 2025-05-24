from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.services.auth_service import AuthService
from src.entities.user import LoginUserRequest
from src.utils.helpers import handle_database_exception
import os
from dotenv import load_dotenv

load_dotenv()

dev_mode = os.getenv("DEV_MODE")

router = APIRouter(
  prefix="/auth",
  tags=["auth"]
)

@router.post("")
async def login(data: LoginUserRequest):
  try:
    if not data.identifier or not data.password:
      return JSONResponse(status_code=422, content={"message": "Todos os campos são obrigatórios"})

    # Repository
    if dev_mode == "True":
      from src.repositories.user_repository import UserRepository
      repo = UserRepository()
    else:
      from src.mock.user_repository_mock import UserRepositoryMock
      repo = UserRepositoryMock()
    
    # Service
    login = AuthService(repo).login(
      identifier=data.identifier,
      password=data.password
    )
    if login == "is_first":
      return JSONResponse(status_code=200, content={"message": "Primeiro login, troque sua senha", "token": ""})
    return JSONResponse(status_code=200, content={"message":"Logado com Sucesso", "token": login})
  except Exception as e:
    handle_database_exception(e, "LoginUser")