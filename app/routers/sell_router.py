from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import sell_controller
from app.utils.response import success_response, custom_sell_data
from app.auth.dependency import get_current_user
from app.schemas.sell import SellCreate, SellOut

router = APIRouter()

@router.get("/all", dependencies=[Depends(get_current_user)])
def get_sell_data(db: Session = Depends(get_db)):
    data = sell_controller.get_sell_data(db)
    
    if not data:
        raise HTTPException(status_code=404, detail="No sell data found")
    
    return success_response(custom_sell_data(data))

@router.get("/{sell_id}", dependencies=[Depends(get_current_user)])
def get_sell_by_id(sell_id: int, db: Session = Depends(get_db)):
    sell = sell_controller.get_sell_by_id(sell_id, db)
    
    if not sell:
        raise HTTPException(status_code=404, detail="Sell data not found")
    
    return success_response(custom_sell_data(sell))

@router.post("/add", dependencies=[Depends(get_current_user)])
def create_sell(sell_data: SellCreate, db: Session = Depends(get_db)):
    new_sell = sell_controller.create_sell(sell_data, db)
    
    if not new_sell:
        raise HTTPException(status_code=400, detail="Failed to create sell data")
    
    return success_response(new_sell, message="Sell data created successfully")

