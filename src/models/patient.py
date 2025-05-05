from sqlalchemy import Column, Integer, String, Date, Text, Enum, TIMESTAMP, func, CHAR
from scripts.base import Base
from src.enums.gender_enum import GenderEnum


class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False, index=True)
    cpf = Column(CHAR(11), unique=True, nullable=False)
    rg = Column(String(20))
    birth_date = Column(Date)
    phone = Column(String(20))
    email = Column(String(255))
    address = Column(Text)
    gender = Column(Enum(GenderEnum))
    created_at = Column(TIMESTAMP, server_default=func.now())
