from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.auth.dependency import get_current_user
from app.database import get_db
from app.controllers import user_controller
from app.utils.response import success_response

router = APIRouter()

@router.get("/all")
def get_all_users(db: Session = Depends(get_db)):
    data = user_controller.get_all_users(db)

    if not data: 
        raise HTTPException(status_code=404, detail="No users found")
    
    return success_response(data)

@router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    data = user_controller.get_user_by_id(db, user_id)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return success_response(data)

