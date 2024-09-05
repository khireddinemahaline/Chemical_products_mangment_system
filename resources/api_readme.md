# Chemical Products Management API

## Overview
This API allows you to manage chemical products, orders, and user accounts. It supports various HTTP methods for interacting with these resources.

## Endpoints

### Users

- **Retrieve Current Users**
  - **HTTP Method**: GET
  - **URI**: `/api/users`
  - **Action**: Retrieve a list of current users.

- **Retrieve User Information Based on ID**
  - **HTTP Method**: GET
  - **URI**: `/api/users/[id]`
  - **Action**: Retrieve user information based on their ID.

- **Create or Update a User Account**
  - **HTTP Method**: POST
  - **URI**: `/api/users`
  - **Action**: Create or update a user account.

- **Create or Update a User Account**
  - **HTTP Method**: PUT
  - **URI**: `/api/users/[id]`
  - **Action**: Create or update a user account.

- **Delete User Based on ID**
  - **HTTP Method**: DELETE
  - **URI**: `/api/users/[id]`
  - **Action**: Delete a user based on their ID.

### Chemical Products

- **Retrieve List of All Chemical Products**
  - **HTTP Method**: GET
  - **URI**: `/api/products`
  - **Action**: Retrieve a list of all chemical products.

- **Retrieve Details of a Specific Chemical Product**
  - **HTTP Method**: GET
  - **URI**: `/api/products/[id]`
  - **Action**: Retrieve details of a specific chemical product.

- **Add a New Chemical Product to the Inventory**
  - **HTTP Method**: POST
  - **URI**: `/api/products`
  - **Action**: Add a new chemical product to the inventory.

- **Update Details of a Specific Chemical Product**
  - **HTTP Method**: PUT
  - **URI**: `/api/products/[id]`
  - **Action**: Update details of a specific chemical product.

- **Delete a Specific Chemical Product**
  - **HTTP Method**: DELETE
  - **URI**: `/api/products/[id]`
  - **Action**: Delete a specific chemical product.

### Orders

- **Retrieve List of All Orders link to a specifeque user**
  - **HTTP Method**: GET
  - **URI**: `/api/users/[id]/orders`
  - **Action**: Retrieve a list of all orders.

- **Retrieve Details of a Specific Order**
  - **HTTP Method**: GET
  - **URI**: `/api/orders/[id]`
  - **Action**: Retrieve details of a specific order.

- **Place a New Order for Chemical Products**
  - **HTTP Method**: POST
  - **URI**: `/api/orders`
  - **Action**: Place a new order for chemical products.

- **Update Status of a Specific Order**
  - **HTTP Method**: PUT
  - **URI**: `/api/orders/[id]`
  - **Action**: Update the status of a specific order.

- **Delete a Specific Order**
  - **HTTP Method**: DELETE
  - **URI**: `/api/orders/[id]`
  - **Action**: Cancel a specific order.

### Order_staus

- **Retrieve order_staus linked to the order**
  - **HTTP Method**: GET
  - **URI**: `/api/orders/[id]/order_status`
  - **Action**: Retrieve a list of oder_status.

- **Update Status of a Specific Order**
  - **HTTP Method**: PUT
  - **URI**: `/api/order_status/[id]`
  - **Action**: Update the status of a specific order.


