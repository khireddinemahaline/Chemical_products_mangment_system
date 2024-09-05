#!/usr/bin/python3

from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.order_status import Order_status
from models.orders import Order
from models import storage


@app_views.route("/orders/<string:order_id>/order_status", strict_slashes=False,
                 methods=['GET'])
def get_orders_status(order_id):
    retrive = []
    order = storage.get(Order, order_id)
    if order is None:
        abort(404)
    for status in order.order_status:
        retrive.append(status.to_dict())
    return jsonify(retrive)


@app_views.route("/order_status/<string:status_id>", strict_slashes=False,
                 methods=['GET'])
def get_by_id_orders_status(status_id):
    status = storage.get(Order_status, status_id)
    if status is None:
        abort(404)
    return jsonify(status.to_dict())


@app_views.route("/order_status/<string:status_id>", strict_slashes=False,
                 methods=['PUT'])
def update_order_status(status_id):
    status = storage.get(Order_status, status_id)
    if status is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "not a json"}), 400)
    for key, values in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(status, values)
    order.save()
    return make_response(jsonify(status.to_dict()), 201)