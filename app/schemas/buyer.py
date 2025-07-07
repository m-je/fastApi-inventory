from pydantic import BaseModel

class BuyerCreate(BaseModel):
    name: str
    email: str | None = None

class BuyerOut(BuyerCreate):
    id: int
    class Config:
        orm_mode = True