from typing import Optional
from datetime import date
from src.enums.gender_enum import GenderEnum

class PatientEntity:
    patient_id: Optional[int] = None
    name: str
    cpf: str
    rg: Optional[str] = None
    birth_date: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    gender: Optional[GenderEnum] = None
    folder_path: Optional[str] = None
    
    def __init__(self, name: str, cpf: str, rg: Optional[str] = None, 
                 birth_date: Optional[date] = None, phone: Optional[str] = None,
                 email: Optional[str] = None, address: Optional[str] = None,
                 gender: Optional[GenderEnum] = None, folder_path: Optional[str] = None,
                 patient_id: Optional[int] = None):
        self.name = name
        self.cpf = cpf
        self.rg = rg
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender.value
        self.folder_path = folder_path
        self.patient_id = patient_id
        
    def validateEmail(self, email: str):
        if len(email) < 3:
            raise ValueError("Email deve ter pelo menos 3 caracteres")
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido")
        return True
        
    def to_dict(self): 
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'cpf': self.cpf,
            'rg': self.rg,
            'birth_date': self.birth_date,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'gender': self.gender.value if self.gender else None,
            'folder_path': self.folder_path
        }
