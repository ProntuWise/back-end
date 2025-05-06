import uvicorn
from fastapi import FastAPI
from scripts.base import Base

app = FastAPI(  
    title="User Management API",
    version="1.0.0",
    description="API for managing users.",
)

@app.get("/")
async def read_root():
    return {"message": "API is running successfully!"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
