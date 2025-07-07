from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.auth.dependency import get_current_user
from app.models import Product
from app.schemas import ProductBulkCreate, ProductUpdate, ProductOut
from app.database import get_db
from app.controllers import product_controller
from app.utils.response import success_response

router = APIRouter()

@router.get("/all", dependencies=[Depends(get_current_user)])
def get_all_products(db: Session = Depends(get_db)):
    data = product_controller.get_all_products(db)
    if not data: 
        raise HTTPException(status_code=404, detail="No products found")
    
    return success_response(data)

@router.get("/{product_id}", dependencies=[Depends(get_current_user)])
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = product_controller.get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return success_response(product)

@router.get("/", dependencies=[Depends(get_current_user)])
def read_products(
    db: Session = Depends(get_db),
    name: str = Query(None, description="Filter by product name"),
    min_stock: int = Query(None, description="Filter by minimum stock"),
    max_stock: int = Query(None, description="Filter by maximum stock")
):
    return product_controller.read_products(db, name, min_stock, max_stock)

@router.post("/add", dependencies=[Depends(get_current_user)])
def create_products_bulk(
    payload: ProductBulkCreate, db: Session = Depends(get_db)
):
    return product_controller.create_products_bulk(payload, db)