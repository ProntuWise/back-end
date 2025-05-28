from typing import Optional

from sqlalchemy import TIMESTAMP, Date, Text, Time

from src.enums.appointment_status_enum import AppointmentStatusEnum
from src.enums.appointment_type_enum import AppointmentTypeEnum

class AppointmentEntity:
    appointment_id: Optional[int] = None
    date: Date
    time: Time
    duration: int
    patient_id: int
    user_id: int
    tag_id: int
    description: Text
    status: AppointmentStatusEnum
    appointment_type: AppointmentTypeEnum
    created_at: Optional[TIMESTAMP] = None
    
    def __init__(self, date: Date, time: Time, duration: int,
                 patient_id: int, user_id: int, tag_id: int, description: Text,
                 status: AppointmentStatusEnum, appointment_type: AppointmentTypeEnum,
                 appointment_id: Optional[int] = None, created_at: Optional[TIMESTAMP] = None):
        self.appointment_id = appointment_id
        self.date = date
        self.time = time
        self.duration = duration
        self.patient_id = patient_id
        self.user_id = user_id
        self.tag_id = tag_id
        self.description = description
        self.status = status.value
        self.appointment_type = appointment_type.value
        self.created_at = created_at
        
    def to_dict(self): 
        return {
            'appointment_id': self.appointment_id,
            'date': self.date,
            'time': self.time,
            'duration': self.duration,
            'patient_id': self.patient_id,
            'user_id': self.user_id,
            'tag_id': self.tag_id,
            'description': self.description,
            'status': self.status,
            'appointment_type': self.appointment_type,
            'created_at': self.created_at
        }
    
    