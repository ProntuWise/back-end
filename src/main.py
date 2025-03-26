import uvicorn
from src.models.setup_db import settings
from fastapi import FastAPI


app = FastAPI(
    title="User Management API",
    version="1.0.0",
    description="API for managing users."
)

@app.get("/")
async def read_root():
    return {"message": "API is running successfully!"}

if __name__ == "__main__":
    port = int(settings.PORT)
    uvicorn.run(app, port=port)