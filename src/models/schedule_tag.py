from sqlalchemy import Column, Integer, String, Text
from scripts.base import Base

class ScheduleTagModel(Base):
    __tablename__ = 'ScheduleTag'

    schedule_tag_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
