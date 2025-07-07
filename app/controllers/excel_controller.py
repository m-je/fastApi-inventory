from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import get_db
from datetime import datetime, time, date
from sqlalchemy import between, func, and_, cast, Date
import pandas as pd
import os

from app.models.sell import Sell
from app.models.sell_items import SellItems
from app.models.user import User
from app.models.product import Product
from app.utils.excel import excel_response
from app.utils.response import success_response

def excel_sell(db: Session):
    data = db.query(
        Sell.facture_number,
        Sell.date_sold.label("date"),
        User.name.label("user_name"),
        Product.name.label("product_name"),
        func.sum(SellItems.quantity).label("total_quantity"),
        func.sum(SellItems.price_per_unit * SellItems.quantity).label("total_price")
    ).join(
        User, Sell.user_id == User.id
    ).join(
        SellItems, Sell.id == SellItems.sell_id
    ).join(
        Product, SellItems.product_id == Product.id
    ).group_by(
        Sell.facture_number, Sell.date_sold, User.name, Product.name
    ).all()


    excel = excel_response(
        filename="sell_data.xlsx",
        columns=[
            "Facture Number", "Date", "User Name", "Product Name", "Total Quantity", "Total Price"
        ],
        data=data
    )

    return excel

def excel_sell_tgl(tgl_awal: str, tgl_akhir: str, db: Session):
    try:
        start_date = datetime.strptime(tgl_awal, "%Y-%m-%d").date()
        end_date = datetime.strptime(tgl_akhir, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    data = db.query(
        Sell.facture_number,
        Sell.date_sold.label("date"),
        User.name.label("user_name"),
        Product.name.label("product_name"),
        func.sum(SellItems.quantity).label("total_quantity"),
        func.sum(SellItems.price_per_unit * SellItems.quantity).label("total_price")
    ).join(
        User, Sell.user_id == User.id
    ).join(
        SellItems, Sell.id == SellItems.sell_id
    ).join(
        Product, SellItems.product_id == Product.id
    ).filter(
        cast(Sell.date_sold, Date).between(start_date, end_date),
    ).group_by(
        Sell.facture_number, Sell.date_sold, User.name, Product.name
    ).all()

    excel = excel_response(
        filename=f"sell_data_{tgl_awal}_to_{tgl_akhir}.xlsx",
        columns=[
            "Facture Number", "Date", "User Name", "Product Name", "Total Quantity", "Total Price"
        ],
        data=data
    )

    return excel
