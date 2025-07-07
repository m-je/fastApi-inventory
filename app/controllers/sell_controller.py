from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.sell import Sell
from app.models.sell_items import SellItems
from app.utils.response import success_response
from datetime import date, datetime
from sqlalchemy import func, and_
from app.schemas.sell import SellCreate, SellItemsCreate
from sqlalchemy.orm import joinedload

def get_sell_data(db: Session):
    """
    Fetch all sell data from the database.
    """
    data = (
        db.query(Sell)
        .options(
            joinedload(Sell.user),
            joinedload(Sell.sell_items).joinedload(SellItems.product)
        )
        .all()
    )

    return data

def get_sell_by_id(sell_id: int, db: Session):
    """
    Fetch a specific sell record by its ID.
    """
    sell = (
        db.query(Sell)
        .options(
            joinedload(Sell.user),
            joinedload(Sell.sell_items).joinedload(SellItems.product)
        )
        .filter(Sell.id == sell_id)
        .first()
    )
    if not sell:
        raise HTTPException(status_code=404, detail="Penjualan tidak ditemukan")
    return sell

def create_sell(sell_data: SellCreate, db: Session):
    las_number_today = get_today_last_number(db)
    new_facture_number = generate_facture(las_number_today)

    sell = Sell(
        facture_number=new_facture_number,
        user_id=sell_data.user_id
    )
    db.add(sell)
    db.commit()
    db.refresh(sell)

    for product in sell_data.sell_items:
        sellitems = SellItems(
            sell_id=sell.id,
            product_id=product.product_id,
            quantity=product.quantity,
            price_per_unit=product.price_per_unit,
            total_price=product.quantity * product.price_per_unit
        )
        db.add(sellitems)
    db.commit()
    db.refresh(sell)
    return success_response(sell)

# Get the last sell number for today and generate a new facture number
def get_today_last_number(db: Session) -> int:
    today = date.today()
    
    last_sell = (
        db.query(Sell)
        .filter(func.date(Sell.date_sold) == today)
        .order_by(Sell.id.desc())
        .first()
    )

    if last_sell and last_sell.facture_number:
        try:
            nomor = int(last_sell.facture_number.split("/")[0])
            return nomor
        except:
            return 0
    return 0

def generate_facture(last_number: int = 0, current_date: datetime = None) -> str:
    if current_date is None:
        current_date = datetime.now()

    new_number = last_number + 1
    nomor_urut = f"{new_number:04d}"
    tanggal = f"{current_date.day:02d}"
    tahun_bulan = current_date.strftime("%y%m")

    return f"{nomor_urut}/FP/{tanggal}/{tahun_bulan}"
# end function

