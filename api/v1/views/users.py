#!/usr/bin/python3

from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.users import User
from models import storage


@app_views.route("/users", strict_slashes=False,
                 methods=['GET'])
def get_users():
    retrive = []
    users = storage.all(User).values()
    for user in users:
        retrive.append(user.to_dict())
    return jsonify(retrive)


@app_views.route("/users/<string:user_id>", strict_slashes=False,
                 methods=['GET'])
def get_by_id_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<string:user_id>", strict_slashes=False,
                 methods=['DELETE'])
def delete_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({})


@app_views.route("/users", strict_slashes=False,
                 methods=['POST'])
def create_user():
    if not request.get_json():
        return make_response(jsonify({"error": "not a json"}), 400)
    if 'email' not in request.get_json():
        return make_response(jsonify({"error": "Mising eamil"}), 400)
    if 'password' not in request.get_json():
        return make_response(jsonify({"error": "Mising password"}), 400)
    user = User(**request.get_json())
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route("/users/<string:user_id>", strict_slashes=False,
                 methods=['PUT'])
def update_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "not a json"}), 400)
    for key, values in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(product, values)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)