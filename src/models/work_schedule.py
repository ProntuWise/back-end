from sqlalchemy import Column, Integer, Time, Enum, ForeignKey
from scripts.base import Base
from src.enums.week_day_enum import WeekDayEnum
from src.enums.visit_type_enum import VisitTypeEnum


class WorkSchedule(Base):
    __tablename__ = 'WorkSchedule'

    work_schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    weekday = Column(Enum(WeekDayEnum), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    schedule_tag_id = Column(Integer, ForeignKey('ScheduleTag.schedule_tag_id'))
    visit_type = Column(Enum(VisitTypeEnum), default=VisitTypeEnum.Both)