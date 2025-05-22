from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, func
from scripts.base import Base

class Insurance(Base):
    __tablename__ = "Insurance"

    insurance_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    cnpj = Column(String(14))
    phone = Column(String(20))
    email = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

