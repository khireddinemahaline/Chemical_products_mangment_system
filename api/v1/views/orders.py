#!/usr/bin/python3

from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.orders import Order
from models.users import User
from models import storage
from models.order_status import Order_status


@app_views.route("/users/<string:user_id>/orders", strict_slashes=False,
                 methods=['GET'])
def get_orders(user_id):
    retrive = []
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    for order in user.orders:
        retrive.append(order.to_dict())
    return jsonify(retrive)


@app_views.route("/orders/<string:order_id>", strict_slashes=False,
                 methods=['GET'])
def get_by_id_orders(order_id):
    order = storage.get(Order, order_id)
    if order is None:
        abort(404)
    return jsonify(order.to_dict())


@app_views.route("/orders/<string:order_id>", strict_slashes=False,
                 methods=['DELETE'])
def delete_order(order_id):
    order = storage.get(Order, order_id)
    if order is None:
        abort(404)
    order.delete()
    storage.save()
    return jsonify({})


@app_views.route("/orders", strict_slashes=False,
                 methods=['POST'])
def create_order():
    if not request.get_json():
        return make_response(jsonify({"error": "not a json"}), 400)
    if 'user_id' not in request.get_json():
        return make_response(jsonify({"error": "Mising user_id"}), 400)
    if 'product_id' not in request.get_json():
        return make_response(jsonify({"error": "Mising product_id"}), 400)
    order = Order(**request.get_json())
    storage.new(order)
    storage.save()
    # Automatically create OrderStatus
    order_status = Order_status(order_id=order.id)
    storage.new(order_status)
    storage.save()
    return make_response(jsonify(order.to_dict()), 201)


@app_views.route("/orders/<string:order_id>", strict_slashes=False,
                 methods=['PUT'])
def update_order(order_id):
    order = storage.get(Order, order_id)
    if order is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "not a json"}), 400)
    for key, values in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(order, values)
    order.save()
    return make_response(jsonify(order.to_dict()), 201)