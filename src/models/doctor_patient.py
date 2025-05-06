from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, UniqueConstraint, func
from scripts.base import Base

class DoctorPatient(Base):
    __tablename__ = "doctor_patient"
    __table_args__ = (UniqueConstraint("user_id", "patient_id", name="uq_doctor_patient"),)

    doctor_patient_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"), nullable=False)
    associated_at = Column(TIMESTAMP, server_default=func.now())
