from sqlalchemy import Column, Integer, Date, Time, Text, Enum, TIMESTAMP, ForeignKey, func
from scripts.base import Base
from src.enums.appointment_status_enum import AppointmentStatusEnum

class Schedule(Base):
    __tablename__ = "schedule"

    schedule_id = Column(Integer, primary_key=True, index=True)
    appointment_date = Column(Date, nullable=False, index=True)
    appointment_time = Column(Time, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    description = Column(Text)
    status = Column(Enum(AppointmentStatusEnum), default=AppointmentStatusEnum.Scheduled)
    created_at = Column(TIMESTAMP, server_default=func.now())
