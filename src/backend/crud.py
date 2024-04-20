from sqlalchemy.orm import Session
from schema import ProductCreate, ProductUpdate
from models import ProductModel

# get all (select * from)
def get_products(db: Session) :
    """
    This function returns all products in the database
    """
    return db.query(ProductModel).all()

# get where id=1
def get_product_item(db: Session, product_id: int) :
    """
    This function returns a specific product, acording to the product_id
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# insert into (create)
def create_product(db: Session, product: ProductCreate) :
    """
    This function will create a new product in the database
    """
    # transform view to orm model
    db_product = ProductModel(**product.model_dump())

    # add new product in the databese
    db.add(db_product)

    # commit on databese
    db.commit()

    # refresh the database
    db.refresh(db_product)

    # return the item created to the user
    return db_product


# update wher id=1
def update_product(db: Session, product_id: int, product: ProductUpdate) :
    db_product =  db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None :
        return None
    
    if product.name is not None :
        db_product.name = product.name
    
    if product.category is not None :
        db_product.category = product.category

    if product.description is not None :
        db_product.description = product.description

    if product.price is not None :
        db_product.price = product.price 

    if product.vendor_email is not None :
        db_product.vendor_email = product.vendor_email
    
    db.commit()
    db.refresh(db_product)
    
    return db_product


# delete where id=1
def delete_product(db: Session, product_id: int) :
    db_product =  db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product
