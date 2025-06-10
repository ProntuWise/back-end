

from pydantic import BaseModel

from src.enums.user_type_enum import UserTypeEnum


class CreateUserRequest(BaseModel):
    name: str
    role: UserTypeEnum
    email: str

class LoginUserRequest(BaseModel):
    identifier: str
    password: str

class ChangePasswordRequest(BaseModel):
    identifier: str
    new_password: str