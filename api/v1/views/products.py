#!/usr/bin/python3

from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.products import Product
from models import storage


@app_views.route("/products", strict_slashes=False,
                 methods=['GET'])
def get_products():
    retrive = []
    products = storage.all(Product).values()
    for product in Product:
        retrive.append(product.to_dict())
    return jsonify(retrive)


@app_views.route("/products/<string:product_id>", strict_slashes=False,
                 methods=['GET'])
def get_by_id_product(product_id):
    product = storage.get(Product, product_id)
    if product is None:
        abort(404)
    return jsonify(product.to_dict())


@app_views.route("/products/<string:product_id>", strict_slashes=False,
                 methods=['DELETE'])
def delete_product(user_id):
    product = storage.get(Product, product_id)
    if product is None:
        abort(404)
    storage.delete(product)
    storage.save()
    return jsonify({})


@app_views.route("/products", strict_slashes=False,
                 methods=['POST'])
def create_product():
    if not request.get_json():
        return make_response(jsonify({"error": "not a json"}), 400)
    if 'ref' not in request.get_json():
        return make_response(jsonify({"error": "Mising reffrence"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Mising password"}), 400)
    product = Product(**request.get_json())
    product.save()
    return make_response(jsonify(product.to_dict()), 201)


@app_views.route("/products/<string:product_id>", strict_slashes=False,
                 methods=['PUT'])
def update_product(product_id):
    product = storage.get(Product, product_id)
    if product is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "not a json"}), 400)
    for key, values in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(product, values)
    product.save()
    return make_response(jsonify(product.to_dict()), 201)