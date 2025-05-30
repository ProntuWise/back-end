import jwt
import os
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next):
    # Permitir rotas públicas (como login ou docs) — opcional
    if request.url.path in [
      "/auth/login", 
      "/docs", 
      "/openapi.json"
    ]:
      return await call_next(request)

    token = request.headers.get("Authorization")

    if not token:
      return JSONResponse(
        status_code=401,
        content={"message": "Token de autenticação não fornecido."}
      )

    try:
      scheme, _, token = token.partition(" ")

      if scheme.lower() != "bearer":
        return JSONResponse(
          status_code=401,
          content={"message": "Esquema de autenticação inválido. Use 'Bearer'."}
        )

      payload = jwt.decode(
        token,
        os.getenv("SECRET_KEY"),
        algorithms=["HS256"]
      )

      request.state.user = payload

      response = await call_next(request)
      return response

    except jwt.PyJWTError:
      return JSONResponse(
        status_code=401,
        content={"message": "Token de autenticação inválido."}
      )
    except Exception as e:
      return JSONResponse(
        status_code=500,
        content={"message": f"Erro interno do servidor: {str(e)}"}
      )
