from pydantic import BaseModel

class UserCreate(BaseModel):
    name : str
    email: str
    no_phone: str
    password: str
    is_active: int = 1  # 0 for inactive, 1 for active
    is_superuser: int = 0  # 0 for regular user

class UserOut(BaseModel):
    id: int
    username: str

class UserLogin(BaseModel):
    identifier: str  # Can be username or email
    password: str

    class Config:
        orm_mode = True
