from sqlite3 import IntegrityError

from flask import Blueprint, request

from app.models import user_model
from app.utils.validators import validate_user_json
from app.views import user_views

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
def get_all_users():
    users = user_model.get_all_users()
    return user_views.render_user_list(users)


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = user_model.get_user_by_id(user_id)
    if user is None:
        return user_views.render_error("Usuario no encontrado.", 404)
    return user_views.render_user_detail(user)


@users_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    username, email, password, errors = validate_user_json(data)

    if errors:
        return user_views.render_error(errors, 400)

    try:
        user_id = user_model.create_user(username, email, password)
    except IntegrityError:
        return user_views.render_error("El email ya está registrado.", 409)

    user = user_model.get_user_by_id(user_id)
    return user_views.render_user_created(user)


@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = user_model.get_user_by_id(user_id)
    if user is None:
        return user_views.render_error("Usuario no encontrado.", 404)

    data = request.get_json(silent=True)
    username, email, password, errors = validate_user_json(data)

    if errors:
        return user_views.render_error(errors, 400)

    try:
        user_model.update_user(user_id, username, email, password)
    except IntegrityError:
        return user_views.render_error("El email ya está registrado.", 409)

    updated_user = user_model.get_user_by_id(user_id)
    return user_views.render_user_updated(updated_user)


@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = user_model.get_user_by_id(user_id)
    if user is None:
        return user_views.render_error("Usuario no encontrado.", 404)

    user_model.delete_user(user_id)
    return user_views.render_user_deleted(user_id)
