#!/usr/bin/python3

"""
Product
    products: list of availables products
- order_status will have attr:
    id, created_at, updated_at, class_name inhert from the BaseModel
    ref : the refrence of prod uct
    name : name of products
    description : descrtiption text
    quentity : quentity in the stock
- Product classe will inhert from the BaseModel, Base classes
- we will store data in mysql_DBMS
    * to store the data we will use a python library (sqlalchemy)
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """Product Table Data"""
    __tablename__ = 'products'
    name = Column(String(255), nullable=False)
    ref = Column(String(255), nullable=False, unique=True)
    description = Column(String(2094), nullable=False)
    quentity = Column(Integer, default=1, nullable=False)
    orders = relationship("Order", backref='order', uselist=False,
                          cascade="all, delete")
