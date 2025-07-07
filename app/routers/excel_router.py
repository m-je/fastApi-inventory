from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import excel_controller

router = APIRouter()

@router.get("/sell")
def excel_sell(db: Session = Depends(get_db)):
    return excel_controller.excel_sell(db)

@router.get("/sell/{tgl_awal}/{tgl_akhir}")
def excel_sell_tgl( tgl_awal: str, tgl_akhir: str, db: Session = Depends(get_db)):
    return excel_controller.excel_sell_tgl(tgl_awal, tgl_akhir, db)
   
