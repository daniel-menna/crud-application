from pydantic import BaseModel, PositiveFloat, EmailStr, validators
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel) :
    name : str
    description : Optional[str] = None
    prince : PositiveFloat
    category : str
    vendor_email: EmailStr

class ProductCreate(ProductBase) :
    pass

class ProductUpdate(ProductBase) :
    name : Optional[str] = None
    description : Optional[str] = None
    prince : Optional[PositiveFloat] = None
    category : Optional[str] = None
    vendor_email: Optional[EmailStr] = None

class ProductResponse(ProductBase) :
    id: int
    created_at: datetime

    class config :
        from_atributtes = True


