from pydantic import BaseModel

from src.enums.user_type_enum import UserTypeEnum

class User():
  def __init__ (self, name: str, email: str, password: str, role: UserTypeEnum):
    if self.validateName(name):
      self.name = name,
      nameList = name.split(" ")
      self.username = nameList[0].strip().upper() + nameList[-1].lower()
    if self.validateEmail(email):
      self.email = email
    if self.validateRole(role):
      self.role = role
    self.password = password
    self.is_active = True
    self.is_first = True

  def validateName(self, name: str):
    if len(name) < 3:
      raise ValueError("Nome tem que ter mais de 3 caracteres")
    if name.isalpha():
      raise ValueError("Nome não pode conter números")
    return True
  
  def validateEmail(self, email: str):
    if len(email) < 3:
      raise ValueError("Email tem que ter mais de 3 caracteres")
    if "@" not in email:
      raise ValueError("Email tem que conter @")
    if "." not in email:
      raise ValueError("Email tem que conter .")
    return True
  
  def validateRole(self, role: UserTypeEnum):
    if role not in UserTypeEnum:
      raise ValueError("Tipo de usuário inválido")
    return True


class CreateUserRequest(BaseModel):
  name: str
  role: UserTypeEnum
  email: str
