
from sqlalchemy import Column, Integer, String, Enum, Boolean, TIMESTAMP, func
from scripts.base import Base
from src.enums.user_type_enum import UserTypeEnum

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    role = Column(Enum(UserTypeEnum), nullable=False)
    email = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
