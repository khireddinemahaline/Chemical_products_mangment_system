#!/usr/bin/python3
from flask import Flask, render_template, url_for, request, redirect, session, flash, jsonify
from functools import wraps
from models import storage
from models.products import Product
from models.users import User
from models.orders import Order
from models.order_status import Order_status

app = Flask(__name__)
app.secret_key = 'aef235ef0847657f62f918f89056d2416a602afa5bf21adb058bfab47b0613f7'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html'), 404

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = session.get('user_id')
            user = storage.get(User, user_id)
            if user and user.role == role:
                return f(*args, **kwargs)
            else:
                flash(f'Access denied for {role} only.', 'danger')
                return redirect(url_for('home_product'))
        return decorated_function
    return decorator

@app.route('/home',strict_slashes=False)
@role_required('professor')
def home_product():
    user = None
    user_id = session.get('user_id')
    if user_id:
        user = storage.get(User, user_id)
        if user:
            print(f"User found")  # Debugging output
        else:
            print("User not found in database.")
    else:
        print("No user ID found in session.")
    products = storage.all(Product).values()
    return render_template("home.html", products=products, user=user)

@app.route('/manager', strict_slashes=False, methods=['GET', 'POST'])
@role_required('lab manager')
def manager_page():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        ref = data.get('ref')
        description = data.get('description')
        quentity = data.get('quentity')

        if not name or not ref or not description or quentity is None:
            flash('All fields are required!')
        
        try:
            quentity = int(quentity)  # Convert quantity to integer
            product = Product(name=name, ref=ref, description=description, quentity=quentity)
            storage.new(product)
            product.save()
            return redirect(url_for('manage_page'))

        except ValueError:
            flash('Quantity must be a number!')
        except Exception as e:
            flash(f'Error adding product: {e}')
            
        return redirect(url_for('manager_page'))


    return render_template('admin.html')

@app.route('/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = storage.get(Product, product_id)
    if product:
        product.delete()
        storage.save()
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404





@app.route('/order/<string:product_id>')
@role_required('professor')
def order_page(product_id):
    # Your logic to fetch the product details using product_id
    # and render the order page
    user_id = session.get('user_id')
    user = storage.get(User, user_id)
    product = storage.get(Product, product_id)
    return render_template('order_page.html', product_id=product_id,product=product, user=user)


# the route for the sign in 
# check if the email entred and the password are == to the one in DB
@app.route('/signin', strict_slashes=False, methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = storage.all(User).values()
        for user in users:
            if user and user.password == password and user.email == email:
                session['user_id'] = user.id  # Ensure user.id is a string
                if user.role == 'professor':
                    return redirect(url_for('home_product'))
                elif user.role == 'lab manager':
                    return redirect(url_for('manager_page'))
        else:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('signin'))
    return render_template('signin.html')


# take the new data (User) and save it to the DB
@app.route('/', strict_slashes=False)
@app.route("/signup", strict_slashes=False, methods=["GET","POST"])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        role = request.form.get('role')

        new_user = User(email=email, password=password,
                        first_name=first_name, last_name=last_name, role=role)
        storage.new(new_user)
        storage.save()

        return redirect(url_for('success_page'))
    return render_template('signup.html')

# when the regestertion success
@app.route('/success')
def success_page():
    return "User registered successfully!"


@app.route('/submit_order/<string:product_id>', methods=['POST'])
@role_required('professor')
def submit_order(product_id):
    quantity = request.form.get('quentity')
    if not quantity:  # Check if quentity is empty or None
        flash('Quantity is required.', 'danger')
        return redirect(url_for('order_page', product_id=product_id))
    # Retrieve the product using the product_id
    product = storage.get(Product, product_id)

    if product and int(quantity) > 0 and int(quantity) <= product.quentity:
        # Logic to save the order in the database
        # For example, create a new Order object and save it
        new_order = Order(product_id=product_id, quantity=quantity, user_id=session.get('user_id'), quentity=quantity)
        storage.new(new_order)
        storage.save()

        order_status = Order_status(order_id=new_order.id)
        storage.new(order_status)
        storage.save()
        
        # Optionally, you can reduce the quantity of the product
        product.quentity -= int(quantity)
        storage.save()

        flash('Order placed successfully!', 'success')
    else:
        flash('Invalid quantity selected.', 'danger')

    return redirect(url_for('home_product'))



@app.route('/dashbord', strict_slashes=False)
@role_required('professor')
def dashbord_page():
    user_id = session.get('user_id')
    user = storage.get(User, user_id)
    products = []
    order_details = {}  # Dictionary to hold product_id and its corresponding quantity and status

    for order in user.orders:
        product = storage.get(Product, order.product_id)
        if product:
            products.append(product)
            order_details[product.id] = {
                'quantity': order.quentity,
                'status': [status.status for status in order.order_status]
            }

    return render_template('dashbord.html', user=user, products=products, order_details=order_details)





if __name__ == '__main__':
    host='0.0.0.0'
    port='5002'
    app.run(host=host, port=port)
    




