from pydantic import BaseModel
from datetime import datetime
from src.enums.user_type_enum import UserTypeEnum

class User:
    def __init__(self, name: str, email: str, password: str, role: UserTypeEnum):
        # Validações
        self.validateName(name)
        self.validateEmail(email)
        self.validateRole(role)

        self.name = name
        prepositions = {"de", "da", "do", "das", "dos"}
        name_parts = [part for part in name.strip().split() if part.lower() not in prepositions]

        if len(name_parts) > 1:
            initials = ''.join([part[0].upper() for part in name_parts[:-1]])
            last_name = name_parts[-1].capitalize()
            self.username = last_name + initials
        else:
            self.username = name_parts[0].capitalize()

        self.email = email
        self.password = password
        self.role = role
        self.is_active = True
        self.is_first = True

    def validateName(self, name: str):
        if len(name) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        if any(char.isdigit() for char in name):
            raise ValueError("Nome não pode conter números")
        return True

    def validateEmail(self, email: str):
        if len(email) < 3:
            raise ValueError("Email deve ter pelo menos 3 caracteres")
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido")
        return True

    def validateRole(self, role: UserTypeEnum):
        if not isinstance(role, UserTypeEnum):
            raise ValueError("Tipo de usuário inválido")
        return True


class CreateUserRequest(BaseModel):
    name: str
    role: UserTypeEnum
    email: str

class LoginUserRequest(BaseModel):
    identifier: str
    password: str