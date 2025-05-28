from datetime import date, time
from pydantic import BaseModel
from src.enums.appointment_status_enum import AppointmentStatusEnum
from src.enums.appointment_type_enum import AppointmentTypeEnum


class AppointmentCreateRequest(BaseModel):
    date: date
    time: time
    duration: int
    patient_id: int
    user_id: int
    tag_id: int
    description: str
    status: AppointmentStatusEnum
    appointment_type: AppointmentTypeEnum
