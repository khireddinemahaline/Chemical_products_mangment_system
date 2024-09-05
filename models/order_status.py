#!/usr/bin/python3
"""
Order_status
    oser_status: approved / Not approved
- order_status will have attr:
    id, created_at, updated_at, class_name inhert from the BaseModel
    order_id : the orders to change thier states 
    status : to maniplate the status of orders # true , false
- Order_status classe will inhert from the BaseModel, Base classes
- we will store data in mysql_DBMS
    * to store the data we will use a python library (sqlalchemy)
"""

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Enum
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Order_status(BaseModel, Base):
    __tablename__ = 'order_status'
    order_id = Column(String(60), ForeignKey('orders.id', ondelete="CASCADE",
                                            onupdate="CASCADE"), nullable=False) 
    status = Column(Enum("pending", "confirmed", name="order_status"), default="pending", nullable=False)


