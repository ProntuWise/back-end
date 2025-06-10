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

class AppointmentUpdateRequest(BaseModel):
    date: str | None = None
    time: str | None = None
    duration: int | None = None
    patient_id: int | None = None
    user_id: int | None = None
    tag_id: int | None = None
    description: str | None = None
    status: AppointmentStatusEnum | None = None
    appointment_type: AppointmentTypeEnum | None = None
