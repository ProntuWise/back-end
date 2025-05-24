from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException

def handle_database_exception(e: Exception, context: str = ""):
  if isinstance(e, IntegrityError):
    raise HTTPException(status_code=409, detail={"message":"Conflito de integridade no banco de dados."})
  elif isinstance(e, SQLAlchemyError):
    raise HTTPException(status_code=500, detail={"message":"Erro ao acessar o banco de dados."})
  else:
    raise HTTPException(status_code=500, detail={"message":"Erro inesperado ao processar a requisição."})