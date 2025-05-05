import uvicorn
from fastapi import FastAPI
from scripts.base import Base
# from scripts.db_connection import engine
# from contextlib import asynccontextmanager

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Executado na startup
    # Base.metadata.create_all(bind=engine)
#     yield
#     # Executado no shutdown (se necessário, adicione lógica aqui)

app = FastAPI(  
    title="User Management API",
    version="1.0.0",
    description="API for managing users.",
    # lifespan=lifespan
)

@app.get("/")
async def read_root():
    return {"message": "API is running successfully!"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
