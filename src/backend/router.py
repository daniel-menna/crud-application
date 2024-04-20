from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schema import ProductCreate, ProductResponse, ProductUpdate
from typing import List
from crud import (
    create_product,
    update_product,
    delete_product,
    get_products,
    get_product_item,
)

router = APIRouter()

### Router to get an item
@router.get("/products/{product_id}", response_model = ProductResponse)
def read_item(product_id: int, db: Session = Depends(get_db)) :
    product_item = get_product_item(db=db, product_id=product_id)
    if product_item is None :
        raise HTTPException(status_code=404, detail="Product not found in our database, please check the ID and try again.")
    return product_item

### Router to get all items
@router.get("/products/", response_model=List[ProductResponse])
def read_all_items(db: Session = Depends(get_db)) :
    products = get_products(db)
    return products

### Router to update an item
@router.put("/products/{product_id}", response_model = ProductResponse)
def update_item(product_id: int, product: ProductUpdate, db: Session=Depends(get_db)) :
    updated_item = update_product(db=db, product_id=product_id, product=product)
    if updated_item is None :
        raise HTTPException(status_code=404, detail="Product not found in our database, please check the ID and try again.")
    return updated_item
   

### Router to create an item
@router.post("/products/", response_model = ProductResponse)
def new_product(product: ProductCreate, db: Session=Depends(get_db)) :
    return create_product(product=product, db=db )

### Router to delete an item
@router.delete("/products/{product_id}", response_model = ProductResponse)
def del_product(product_id: int, db: Session = Depends(get_db)) :
    product_deleted = delete_product(product_id=product_id, db=db)
    if product_deleted is None :
        raise HTTPException(status_code=404, detail="Product not found in our database, please check the ID and try again.")
    return product_deleted