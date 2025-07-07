from pydantic import BaseModel, Field
from typing import List

class ProductBase(BaseModel):
    name: str
    price: float = Field(gt=0, description="Price must be greater than zero")
    color: str
    size: str | None = None
    weight: float | None = None
    image_url: str | None = None
    description: str | None = None
    category: str | None = None
    brand: str | None = None
    stock: int = Field(ge=0, description="Stock must be zero or positive")
    status: int = Field(ge=0, le=1, description="Status must be 0 (inactive) or 1 (active)")

class ProductBulkCreate(BaseModel):
    products: List[ProductBase]

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    color: str | None = None
    size: str | None = None
    weight: float | None = None
    image_url: str | None = None
    description: str | None = None
    category: str | None = None
    brand: str | None = None
    stock: int | None = None
    status: int | None = None

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True