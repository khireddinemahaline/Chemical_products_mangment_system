# Chemical_products_mangment_system
web-based application designed to streamline the management of chemical products used in university laboratories, The system facilitates ordering, inventory management, and product tracking between administrators and professors.
- **Live Project**: [Chemical Products Management System](https://www.mhalaine.tech/)
- **Blog Post**: [Project Blog Article](https://www.linkedin.com/pulse/project-overview-streamlining-chemical-product-labs-m-halaine-ltdaf/?trackingId=k7BMd6a4Qj27qfWepLFckA%3D%3D)
- **Author's LinkedIn**: [M'halaine Khireddine LinkedIn](https://www.linkedin.com/in/khireddine-mhalaine/)

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/khireddinemahaline/Chemical_products_mangment_system.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Chemical_products_mangment_system
    ```

3. **Set up a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database**:  
   Ensure you have a MySQL database running, then configure the `.env` file with your database credentials.
   ```bash
   cat setup_mysql_dev.sql
   ```

7. **Start the Flask server**:
    ```bash
    python3 -m run:app
    ```

8. **Access the app**:  
   Open your browser and navigate to [http://127.0.0.1:5002](http://127.0.0.1:5002).

## Usage

The system allows users with specific roles to perform the following actions:

- **Lab Manager**: View inventory, approve orders, update product details.
- **Professors**: Place chemical orders, track the status of submitted orders.

### Steps to use:

1. **Sign up**:  
   Users can register either as lab managers or professors.

2. **Login**:  
   Users log in and are redirected to the appropriate dashboard based on their role.

3. **Manage Orders**:  
   - Lab managers can manage and track orders.
   - Professors can create new orders and check their statuses.

## Contributing

We welcome contributions! If you'd like to contribute to the project:

1. Fork the repository.

2. Create a new feature branch:

    ```bash
    git checkout -b feature-name
    ```

3. Make your changes and commit them:

    ```bash
    git commit -m "Add new feature"
    ```

4. Push to the branch:

    ```bash
    git push origin feature-name
    ```

5. Create a pull request.


## License
This project is licensed under the [Proprietary Custom License](./LICENSE).
