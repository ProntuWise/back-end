from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey, TIMESTAMP, func
from scripts.base import Base
from src.enums.recurrence_enum import RecurrenceEnum


class BlockedSchedule(Base):
    __tablename__ = 'BlockedSchedule'

    blocked_schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
    recurrence = Column(Enum(RecurrenceEnum), default=RecurrenceEnum.None_)
    schedule_tag_id = Column(Integer, ForeignKey('ScheduleTag.schedule_tag_id'))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())