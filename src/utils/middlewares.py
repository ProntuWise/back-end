import jwt
import os
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime

class AuthMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next):
    if request.url.path in [
      "/",
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
      
      try:
        payload = jwt.decode(
          token,
          "secret_key",
          algorithms=["HS256"]
        )
        print("Payload decodificado:", payload)
        if "exp" in payload:
          print("Tempo de expiração:", datetime.fromtimestamp(payload["exp"]))

        request.state.user = payload

        response = await call_next(request)
        return response
      except jwt.ExpiredSignatureError as e:
        print("Erro de expiração:", str(e))
        return JSONResponse(
          status_code=401,
          content={"message": "Token de autenticação expirado."}
        )
      except jwt.InvalidTokenError as e:
        print("Erro de token inválido:", str(e))
        return JSONResponse(
          status_code=401,
          content={"message": "Token de autenticação inválido."}
        )
      except Exception as e:
        print("Erro inesperado:", str(e))
        return JSONResponse(
          status_code=500,
          content={"message": f"Erro interno do servidor: {str(e)}"}
        )
    except Exception as e:
      print("Erro geral:", str(e))
      return JSONResponse(
        status_code=500,
        content={"message": f"Erro interno do servidor: {str(e)}"}
      )
