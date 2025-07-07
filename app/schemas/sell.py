from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class SellItemsBase(BaseModel):
    product_id: int
    quantity: int = Field(gt=0, description="Quantity must be greater than zero")
    price_per_unit: float = Field(gt=0, description="Price per unit must be greater than zero")

class SellItemsCreate(SellItemsBase):
    pass

class SellItems(SellItemsBase):
    id: int
    total_price: float = Field(gt=0, description="Total price must be greater than zero")

    class Config:
        orm_mode = True

class SellBase(BaseModel):
    user_id: int

class SellCreate(SellBase):
    sell_items: List[SellItemsCreate]

class Sell(SellBase):
    id: int
    facture_number: str
    date_sold: datetime  # Using string for simplicity, can be datetime if needed
    sell_items: List[SellItems] = []

    class Config:
        orm_mode = True

# SellItemOut is used to represent the output of a sell item with product details
class ProductOut(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        orm_mode = True

class SellItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    price_per_unit: float
    total_price: float
    product: ProductOut

    class Config:
        orm_mode = True

class CustomerOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class SellOut(BaseModel):
    id: int
    facture_number: str
    user_id: int
    date_sold: datetime
    customer: CustomerOut
    sell_items: List[SellItemOut]

    class Config:
        orm_mode = True

