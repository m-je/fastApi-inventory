from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.response import success_response


def get_all_users(db: Session):
    data = db.query(User).all()
    return data

def get_user_by_id(db: Session, user_id: int):
    data = db.query(User).filter(User.id == user_id).first()
    return data
    