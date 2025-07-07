from sqlalchemy import Column, Integer, String, Float
from app.database import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=True)  # Assuming price can be nullable for some reason
    color = Column(String(50), nullable=False)
    size = Column(String(50), nullable=True)
    weight = Column(Float, nullable=True)
    image_url = Column(String(255), nullable=True)
    description = Column(String(500), nullable=True)
    category = Column(String(100), nullable=True)
    brand = Column(String(100), nullable=True)
    status = Column(Integer, default=1)  # 0 for inactive, 1 for active
    stock = Column(Integer, default=0)

    sell_items = relationship("SellItems", back_populates="product", cascade="all, delete")
