from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import or_, and_
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from app.auth.jwt_handler import create_access_token
from app.schemas.user import UserLogin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.no_phone == user.no_phone).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="No Hp sudah digunakan")

    hashed_password = pwd_context.hash(user.password)
    cleaned_username = user.email.split("@")[0]
    new_user = User(
        name=user.name,
        email=user.email,
        no_phone=user.no_phone,
        username=cleaned_username, 
        password=hashed_password
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(user: UserLogin, db: Session):
    identifier = user.identifier
    is_email = "@" in identifier

    if is_email:
        # Login pakai email → harus cocok 100%
        db_user = db.query(User).filter(User.email == identifier, User.is_active == True).first()
    else:
        # Login pakai username atau no_hp
        db_user = db.query(User).filter(
            or_(
                User.username == identifier,
                User.no_phone == identifier
            ),
            User.is_active == True
        ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="User tidak ditemukan atau akun tidak aktif")
    
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Username / No HP / Email atau password salah")
    
    # Generate JWT token
    token = create_access_token({"sub": user.identifier})
    return {"access_token": token, "token_type": "bearer"}
