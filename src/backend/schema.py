from pydantic import BaseModel, PositiveFloat, EmailStr, validators
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel) :
    name : str
    description : str
    prince : PositiveFloat
    category : str
    vendor_email: EmailStr

class ProductCreate(ProductBase) :
    pass




