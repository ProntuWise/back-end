import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.routes.user_routes import router as user_router

app = FastAPI(  
    title="User Management API",
    version="1.0.0",
    description="API for managing users.",
)

@app.get("/")
async def read_root():
    return {"message": "API is running successfully!"}

app.include_router(user_router)

# ===========================
# Custom Exception Handlers
# ===========================
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
    errors = exc.errors()
    messages = []
    for err in errors:
        loc_parts = [str(i) for i in err.get("loc", []) if i != "body"]
        loc = ".".join(loc_parts)
        
        type_map = {
            "missing": "campo ausente:",
            "value_error.missing": "campo ausente:",
            "type_error.integer": "tipo inválido, esperado inteiro",
        }
        typ = err.get("type", "")
        typ_pt = type_map.get(typ, typ)
        
        msg_map = {
            "Field required": "Campo obrigatório",
        }
        msg = err.get("msg", "")
        msg_pt = msg_map.get(msg, msg)
        
        messages.append(f"{typ_pt} {loc} - {msg_pt}")

    full_message = "; ".join(messages)

    return JSONResponse(
        status_code=422,
        content={"message": full_message}
    )

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
