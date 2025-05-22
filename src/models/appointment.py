from sqlalchemy import Column, Integer, Date, Time, Enum, ForeignKey, TIMESTAMP, Text, func
from scripts.base import Base
from src.enums.appointment_status_enum import AppointmentStatusEnum
from src.enums.appointment_type_enum import AppointmentTypeEnum


class Appointment(Base):
    __tablename__ = 'Appointment'

    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    duration = Column(Integer, nullable=False)
    patient_id = Column(Integer, ForeignKey('Patient.patient_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('ScheduleTag.schedule_tag_id'))
    description = Column(Text)
    status = Column(Enum(AppointmentStatusEnum), default=AppointmentStatusEnum.Scheduled)
    appointment_type = Column(Enum(AppointmentTypeEnum), default=AppointmentTypeEnum.First_Visit)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
