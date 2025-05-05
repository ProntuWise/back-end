from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, func
from scripts.base import Base

class PatientInfo(Base):
    __tablename__ = "patient_info"

    patient_info_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"), nullable=False)
    file_identifier = Column(String(255), nullable=False)
    description = Column(Text)
    uploaded_at = Column(TIMESTAMP, server_default=func.now())
