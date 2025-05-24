
from sqlalchemy import Column, Integer, String, Enum, Boolean, TIMESTAMP, func
from scripts.base import Base

from src.enums.user_type_enum import UserTypeEnum

class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    role = Column(Enum(UserTypeEnum), nullable=False)
    email = Column(String(255))
    is_first = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
