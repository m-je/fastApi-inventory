from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base   
import datetime

class Sell(Base):
    __tablename__ = "sells"

    id = Column(Integer, primary_key=True, index=True)
    facture_number = Column(String(50), unique=True, nullable=False)  # Unique invoice number
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)  # Assuming buyer_id is a foreign key to buyers table
    date_sold = Column(DateTime, default=datetime.datetime.utcnow)  # Storing date as string for simplicity
    status = Column(Integer, default=1)  # 0 for cancelled, 1 for completed

    sell_items = relationship("SellItems", back_populates="sell", cascade="all, delete")
    user = relationship("User", back_populates="sells")  # Assuming User has a relationship defined