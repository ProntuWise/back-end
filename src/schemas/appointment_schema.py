from datetime import datetime
from pydantic import BaseModel
from src.enums.appointment_status_enum import AppointmentStatus
from src.enums.appointment_type_enum import AppointmentType


class AppointmentCreateRequest(BaseModel):
    appointment_name: str
    patient_id: int
    doctor_id: int
    date_time: datetime
    appointment_type: AppointmentType
    notes: str | None = None

class AppointmentUpdateRequest(BaseModel):
    date_time: datetime | None = None
    appointment_type: AppointmentType | None = None
    status: AppointmentStatus | None = None
    notes: str | None = None

