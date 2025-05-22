from sqlalchemy import Column, Integer, ForeignKey
from scripts.base import Base

class ScheduleConfig(Base):
    __tablename__ = 'ScheduleConfig'

    schedule_config_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    default_duration = Column(Integer, default=60)
    first_visit_duration = Column(Integer, default=90)
    followup_duration = Column(Integer, default=30)
