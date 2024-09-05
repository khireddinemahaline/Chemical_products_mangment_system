#!/usr/bin/python3
"""
Model documntation: 
      - all classes are imported here
      - storage data are imported here   
"""

from models.users import User
from models.orders import Order
from models.order_status import Order_status
from models.products import Product
from models.engine.db_storage import DBStorage


classes = { "User": User, "Order": Order,
           "Order_status": Order_status, "Product":Product }
storage = DBStorage()
storage.reload()

