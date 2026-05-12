from flask import jsonify


def render_user_list(users):
    return jsonify([dict(user) for user in users])


def render_user_detail(user):
    return jsonify(dict(user))


def render_user_created(user):
    return jsonify(dict(user)), 201


def render_user_updated(user):
    return jsonify(dict(user))


def render_user_deleted(user_id):
    return jsonify({"message": "Usuario eliminado correctamente.", "id": user_id})


def render_error(message, status_code):
    return jsonify({"error": message}), status_code
