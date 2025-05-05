from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey, UniqueConstraint, func
from scripts.base import Base

class PatientInsurance(Base):
    __tablename__ = "patient_insurance"
    __table_args__ = (UniqueConstraint("patient_id", "insurance_id", name="uq_patient_insurance"),)

    patient_insurance_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"), nullable=False)
    insurance_id = Column(Integer, ForeignKey("insurance.insurance_id"), nullable=False)
    card_number = Column(String(100))
    expiration_date = Column(Date)
    plan_name = Column(String(255))
    associated_at = Column(TIMESTAMP, server_default=func.now())
