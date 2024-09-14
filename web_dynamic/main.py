from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from models import storage, Product, User, Order, Order_status
from .decorator import role_required
import uuid

main_bp = Blueprint('main', __name__)


@main_bp.route('/home',strict_slashes=False)
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
    return render_template("home.html", products=products, user=user, cache_id=uuid.uuid4())


@main_bp.route('/order/<string:product_id>')
@role_required('professor')
def order_page(product_id):
    # Your logic to fetch the product details using product_id
    # and render the order page
    user_id = session.get('user_id')
    user = storage.get(User, user_id)
    product = storage.get(Product, product_id)
    return render_template('order_page.html', product_id=product_id,product=product, user=user, cache_id=uuid.uuid4())


# the route for the sign in 
# check if the email entred and the password are == to the one in DB



@main_bp.route('/submit_order/<string:product_id>', methods=['POST'])
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

    return redirect(url_for('main.home_product'))



@main_bp.route('/dashbord', strict_slashes=False)
@role_required('professor')
def dashbord_page():
    user_id = session.get('user_id')
    user = storage.get(User, user_id)
    products = []
    order_details = {}  # Dictionary to hold product_id and its corresponding quantity and status

    for order in user.orders:
        product = storage.get(Product, order.product_id)
        if product:
            # Add product to products list if not already present
            if product not in products:
                products.append(product)

            # Ensure a list exists for this product's orders in order_details
            if product.id not in order_details:
                order_details[product.id] = []

            # Always append a new entry for every order of the product
            order_details[product.id].append({
                'quantity': order.quentity,
                'status': order.order_status.status
            })
               

    return render_template('dashbord.html', user=user, products=products, order_details=order_details, cache_id=uuid.uuid4())
