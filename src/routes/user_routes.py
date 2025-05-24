from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.services.user_service import UserServices
from src.entities.user import CreateUserRequest

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.post("/")
def createUser(user: CreateUserRequest):
  try:
    # Validate user data
    if not user.name or not user.email or not user.role:
      return JSONResponse(status_code=422, content={"message": "Todos os campos são obrigatórios"})
    
    # Create user object
    user = UserServices().createUser(user)
    if not user:
      return JSONResponse(status_code=400, content={"message": "Erro ao criar usuário"})
    
    return JSONResponse(status_code=201, content={"message":"Usuário criado com sucesso!"})
  except Exception as e:
    return JSONResponse(status_code=400, content={"message": f"{e}"})