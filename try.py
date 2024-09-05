#!/usr/bin/env python3
import models
from models.users import User

# Retrieve all User objects
users = models.storage.all(User).values()

# Loop through each user object
for user in users:
    # Access the orders relationship for each user
    for order in user.orders:
        print(order)
