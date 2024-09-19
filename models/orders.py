#!/usr/bin/python3
"""
Order
    oser: the orders list that the user had order them
- user will have attr:
    id, created_at, updated_at, class_name inhert from the BaseModel
    quentity : quentity of the product you wanna order
    product_id : the product id will store im the order list
    user_id : who order the product
- Order classe will inhert from the BaseModel, Base classes
- we will store data in mysql_DBMS
    * to store the data we will use a python library (sqlalchemy)
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import event
from models.order_status import Order_status
from models.engine.db_storage import DBStorage


class Order(BaseModel, Base):
    __tablename__ = 'orders'
    quentity = Column(Integer, default=1, nullable=False)
    product_id = Column(String(60), ForeignKey('products.id',
                                               ondelete="SET NULL"),
                        nullable=True)
    user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE",
                                            onupdate="CASCADE"),
                     nullable=False)
    order_status = relationship("Order_status", backref="order",
                                cascade="all, delete-orphan,save-update",
                                uselist=False)
