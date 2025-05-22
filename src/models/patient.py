from sqlalchemy import Column, Integer, String, Date, Text, Enum, TIMESTAMP, func
from scripts.base import Base
from src.enums.gender_enum import GenderEnum


class Patient(Base):
    __tablename__ = 'Patient'

    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    rg = Column(String(20))
    birth_date = Column(Date)
    phone = Column(String(20))
    email = Column(String(255))
    address = Column(Text)
    gender = Column(Enum(GenderEnum))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    folder_path = Column(String(255))
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
