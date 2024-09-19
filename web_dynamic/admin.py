from functools import wraps
from flask import Blueprint, render_template, request, redirect, session, flash, url_for, jsonify
from models import storage, Product, User, Order, Order_status
from .decorator import role_required
import uuid
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/manager', strict_slashes=False, methods=['GET', 'POST'])
@role_required('lab manager')
def manager_page():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        ref = data.get('ref')
        description = data.get('description')
        quentity = data.get('quentity')

        if not name or not ref or not description or quentity is None:
            return jsonify({"error" : "field is required"}), 404
        
        try:
            quentity = int(quentity)  # Convert quantity to integer
            product = Product(name=name, ref=ref, description=description, quentity=quentity)
            storage.new(product)
            product.save()
            return jsonify({"message", "product is added successfuly"})

        except ValueError:
            flash('Quantity must be a number!')
        except Exception as e:
            flash(f'Error adding product: {e}')
            
        return redirect(url_for('manager_page'))

    elif request.method == 'GET':
        products = storage.all(Product).values()
        order_details = {}
        orders = storage.all(Order).values()

        for order in orders:
            product = storage.get(Product, order.product_id)
            if product:
                user_id = order.user_id
                user = storage.get(User, user_id)
                if user:
                    order_details[order.id] = {
                        'quantity': order.quentity,
                        'status': order.order_status.status,
                        'order_id': order.id,
                        'product_name': product.name,
                        'product_ref': product.ref,
                        'user_fname': user.first_name,
                        'user_lname': user.last_name
                    }
        
        # Sort order IDs based on user_fname
        sorted_order_ids = sorted(order_details, key=lambda x: order_details[x].get('user_fname', ''))
        # Reconstruct the sorted dictionary
        order_details_sorted = {order_id: order_details[order_id] for order_id in sorted_order_ids}



    return render_template('admin.html', orders=orders, order_details=order_details_sorted, products=products, cache_id=uuid.uuid4())

@admin_bp.route('/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = storage.get(Product, product_id)
    if product:
        product.delete()
        storage.save()
        return jsonify({"message": "Product removed successfully!"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


@admin_bp.route('/update_order_status', methods=['PUT'])
def update_status():
    data = request.get_json()
    order_id = data.get('order_id')
    new_status = data.get('status')

    if not order_id or not new_status:
        return jsonify({"error": "Missing order ID or status"}), 400

    order = storage.get(Order, order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    order.order_status.status = new_status
    storage.save()
    return jsonify({'message': "status updated successfuly"}), 200
