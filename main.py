import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.routes.user_routes import router as user_router
from src.routes.auth_routes import router as auth_router
from src.routes.schedule_tag_routes import router as schedule_tag_router


app = FastAPI(  
    title="User Management API",
    version="1.0.0",
    description="API for managing users.",
)

@app.get("/")
async def read_root():
    return {"message": "API is running successfully!"}

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(schedule_tag_router)

# ===========================
# Custom Exception Handlers
# ===========================
TYPE_TRANSLATIONS = {
    "missing": "campo ausente",
    "value_error.missing": "campo ausente",
    "type_error.integer": "tipo inválido, esperado inteiro"
}

MSG_TRANSLATIONS = {
    "Field required": "Campo obrigatório",
    "Input should be 'Doctor', 'Admin', 'Unique_Secretary', 'General_Secretary' or 'Full'":
        "Entrada deve ser 'Doctor', 'Admin', 'Unique_Secretary', 'General_Secretary' ou 'Full'",
}

def traduzir_tipo(tipo: str) -> str:
    return TYPE_TRANSLATIONS.get(tipo, tipo)

def traduzir_msg(msg: str) -> str:
    return MSG_TRANSLATIONS.get(msg, msg)

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if isinstance(exc.detail, dict) and "message" in exc.detail:
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail["message"]}
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail)}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    mensagens = []

    for erro in exc.errors():
        loc = ".".join(str(i) for i in erro.get("loc", []) if i != "body")
        tipo = traduzir_tipo(erro.get("type", ""))
        mensagem = traduzir_msg(erro.get("msg", ""))
        mensagens.append(f"{tipo} {loc} - {mensagem}".strip())

    return JSONResponse(
        status_code=422,
        content={"message": "; ".join(mensagens)},
    )

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
