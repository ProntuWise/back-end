from datetime import date
from pydantic import BaseModel
from src.enums.gender_enum import GenderEnum

class PatientCreateRequest(BaseModel):
    name: str
    cpf: str
    rg: str | None = None
    birth_date: date | None = None
    phone: str | None = None
    email: str | None = None
    address: str | None = None
    gender: str | None = None
    folder_path: str | None = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.gender:
            try:
                self.gender = GenderEnum[self.gender]
            except KeyError:
                raise ValueError(f"Gênero inválido. Valores aceitos: {', '.join([g.name for g in GenderEnum])}")
