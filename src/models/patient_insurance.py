from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey, UniqueConstraint, func
from scripts.base import Base

class PatientInsurance(Base):
    __tablename__ = "PatientInsurance"

    patient_insurance_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('Patient.patient_id'), nullable=False)
    insurance_id = Column(Integer, ForeignKey('Insurance.insurance_id'), nullable=False)
    card_number = Column(String(100))
    expiration_date = Column(Date)
    plan = Column(String(255))
    associated_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    __table_args__ = (UniqueConstraint('patient_id', 'insurance_id'),)
