from datetime import datetime, date
from pydantic import BaseModel
from src.enums.week_day_enum import WeekDayEnum
from src.enums.recurrence_enum import RecurrenceEnum

class BlockedScheduleBase(BaseModel):
    doctor_id: int
    date: date
    start_time: datetime
    end_time: datetime
    reason: str | None = None
    recurrence_type: RecurrenceEnum = RecurrenceEnum.None_
    recurrence_end_date: date | None = None
    week_day: WeekDayEnum | None = None

class BlockedScheduleCreate(BlockedScheduleBase):
    pass

class BlockedScheduleUpdate(BaseModel):
    start_time: datetime | None = None
    end_time: datetime | None = None
    reason: str | None = None
    recurrence_type: RecurrenceEnum | None = None
    recurrence_end_date: date | None = None
    week_day: WeekDayEnum | None = None

class BlockedSchedule(BlockedScheduleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 