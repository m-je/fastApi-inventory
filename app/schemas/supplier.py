from pydantic import BaseModel

class SupplierCreate(BaseModel):
    name: str
    contact: str | None = None

class SupplierOut(SupplierCreate):
    id: int
    class Config:
        orm_mode = True