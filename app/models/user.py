from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    no_phone = Column(String(15), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Integer, default=1)  # 0 for inactive, 1 for active
    is_superuser = Column(Integer, default=0)  # 0 for regular user

    sells = relationship("Sell", back_populates="user", cascade="all, delete")
    