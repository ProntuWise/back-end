from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.services.auth_service import AuthService
from src.services.user_service import UserServices
from src.schemas.user_schema import LoginUserRequest, ChangePasswordRequest
from src.utils.helpers import handle_database_exception
import os
from dotenv import load_dotenv

load_dotenv()

dev_mode = os.getenv("DEV_MODE")

router = APIRouter(
  prefix="/auth",
  tags=["auth"]
)

@router.post("/login")
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
  
@router.put("/change-password")
async def changePassword(data: ChangePasswordRequest):
  try:
    if not data.new_password:
      return JSONResponse(status_code=422, content={"message": "A nova senha é obrigatória"})
    
    user = data.identifier
    # Repository
    if dev_mode == "True":
      from src.repositories.user_repository import UserRepository
      repo = UserRepository()
    else:
      from src.mock.user_repository_mock import UserRepositoryMock
      repo = UserRepositoryMock()
    
    # Service
    UserServices(repo).changePassword(identifier=user, new_password=data.new_password)

    return JSONResponse(status_code=200, content={"message": "Senha alterada com sucesso"})
  except Exception as e:
    handle_database_exception(e, "ChangePassword")
