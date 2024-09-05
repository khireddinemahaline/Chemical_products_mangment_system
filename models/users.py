#!/usr/bin/python3
"""
User
    user: is the user will order products from the website
- user will have attr:
    id, created_at, updated_at, class_name inhert from the BaseModel
    first_name : the user first name
    last_name : the user last name
    email : user email
    password : will be a hashed password (sha224) # import hashlib()
    role : professseur || lab_manager
- User classe will inhert from the BaseModel, Base classes
- we will store data in mysql_DBMS
    * to store the data we will use a python library (sqlalchemy)
"""

from sqlalchemy import Column, String, Enum
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User Table Data"""
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    role = Column(String(128), nullable=False)
    orders = relationship("Order", backref='user',
                          cascade="all, delete, save-update")
