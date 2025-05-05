from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, CHAR
from scripts.base import Base

class Insurance(Base):
    __tablename__ = "insurance"

    insurance_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    cnpj = Column(CHAR(14))
    phone = Column(String(20))
    email = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
