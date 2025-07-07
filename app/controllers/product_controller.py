from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductBulkCreate, ProductUpdate, ProductOut
from app.database import get_db
from app.utils.response import success_response
from fastapi import APIRouter, Depends, Query

def read_products (db: Session, name: str = None, min_stock: int = None, max_stock: int = None):
    query = db.query(Product)
    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
    if min_stock is not None:
        query = query.filter(Product.stock >= min_stock)
    if max_stock is not None:
        query = query.filter(Product.stock <= max_stock)
    return success_response(query.all())

def get_all_products(db: Session) :
    return db.query(Product).all()

def get_product_by_id(product_id: int, db: Session) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()

def create_products_bulk(products : ProductBulkCreate, db: Session):
    db_products = []
    for p in products.products:
        db_product = Product(
            name=p.name, 
            price=p.price,
            color=p.color,
            size=p.size,
            weight=p.weight,
            image_url=p.image_url,
            description=p.description,
            category=p.category,
            brand=p.brand,
            status=p.status,
            stock=p.stock
        )
        db.add(db_product)
        db_products.append(db_product)

    db.commit()
    for p in db_products:
        db.refresh(p)
    return success_response(db_products)