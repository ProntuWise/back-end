from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException

def handle_database_exception(e: Exception, context: str = ""):
  if isinstance(e, IntegrityError):
    print(f"IntegrityError in {context}: {e.orig}")
    raise HTTPException(status_code=409, detail={"message":"Conflito de integridade no banco de dados."})
  elif isinstance(e, SQLAlchemyError):
    print(f"SQLAlchemyError in {context}: {e}")
    raise HTTPException(status_code=500, detail={"message":"Erro ao acessar o banco de dados."})
  else:
    print(f"Unexpected error in {context}: {e}")
    raise HTTPException(status_code=500, detail={"message":"Erro inesperado ao processar a requisição."})