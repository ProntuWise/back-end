from sqlalchemy import Column, Integer, Enum, ForeignKey
from scripts.base import Base
from src.enums.week_day_enum import WeekDayEnum 


class BlockedScheduleDay(Base):
    __tablename__ = 'BlockedScheduleDay'

    blocked_schedule_day_id = Column(Integer, primary_key=True, autoincrement=True)
    blocked_schedule_id = Column(Integer, ForeignKey('BlockedSchedule.blocked_schedule_id', ondelete='CASCADE'), nullable=False)
    weekday = Column(Enum(WeekDayEnum), nullable=False)
