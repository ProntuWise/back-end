from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.services.user_service import UserServices
from src.entities.user import CreateUserRequest
from src.utils.helpers import handle_database_exception
import os
from dotenv import load_dotenv

load_dotenv()

dev_mode = os.getenv("DEV_MODE")

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.post("")
async def createUser(user: CreateUserRequest):
  try:
    # Validate user data
    if not user.name or not user.email or not user.role:
      return JSONResponse(status_code=422, content={"message": "Todos os campos são obrigatórios"})
    
    # Repository
    if dev_mode == "True":
      from src.repositories.user_repository import UserRepository
      repo = UserRepository()
    else:
      from src.mock.user_repository_mock import UserRepositoryMock
      repo = UserRepositoryMock()
    
    # Create user object
    user = UserServices(repo).createUser(user)
    if not user:
      return JSONResponse(status_code=400, content={"message": "Erro ao criar usuário"})
    
    return JSONResponse(status_code=201, content={"message":"Usuário criado com sucesso!"})
  except Exception as e:
    handle_database_exception(e, "CreateUser")