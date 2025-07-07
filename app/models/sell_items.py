from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class SellItems(Base):
    __tablename__ = "sell_items"

    id = Column(Integer, primary_key=True, index=True)
    sell_id = Column(Integer, ForeignKey("sells.id"), nullable=False)  # Foreign key to Sell
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)  # Foreign key to Product
    quantity = Column(Integer, nullable=False, default=1)  # Quantity of the product sold
    price_per_unit = Column(Float, nullable=False)  # Price per unit of the product at the time of sale
    total_price = Column(Float, nullable=False)  # Total price for the quantity sold

    sell = relationship("Sell", back_populates="sell_items")
    product = relationship("Product", back_populates="sell_items")  # Assuming Product has a relationship defined

    