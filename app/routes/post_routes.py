from flask import Blueprint, abort, redirect, request, url_for

from app.models import post_model
from app.utils.validators import validate_post_form
from app.views import post_views

post_bp = Blueprint("post", __name__, url_prefix="/post")


@post_bp.route("/list")
def get_all_posts():
    posts = post_model.get_all_posts()
    return post_views.render_post_list(posts)


@post_bp.route("/api/list", methods=["GET"])
def get_all_posts_json():
    posts = post_model.get_all_posts()
    return post_views.render_post_list_partial(posts)


@post_bp.route("/<int:post_id>")
def get_single_post(post_id):
    post = post_model.get_post_by_id(post_id)
    if post is None:
        abort(404)
    return post_views.render_post_detail(post)


@post_bp.route("/create", methods=("GET", "POST"))
def create_post():
    if request.method == "GET":
        return post_views.render_post_create_form()

    title, content, errors = validate_post_form(request.form)
    if errors:
        return post_views.render_post_create_form(errors=errors), 400

    post_model.create_post(title, content)
    return redirect(url_for("post.get_all_posts"))


@post_bp.route("/update/<int:post_id>", methods=("GET", "POST"))
def update_post(post_id):
    post = post_model.get_post_by_id(post_id)
    if post is None:
        abort(404)

    if request.method == "GET":
        return post_views.render_post_update_form(post)

    title, content, errors = validate_post_form(request.form)
    if errors:
        return post_views.render_post_update_form(post, errors=errors), 400

    post_model.update_post(post_id, title, content)
    return redirect(url_for("post.get_all_posts"))


@post_bp.route("/delete/<int:post_id>", methods=["POST"])
def delete_one_post(post_id):
    post = post_model.get_post_by_id(post_id)
    if post is None:
        abort(404)

    post_model.delete_post(post_id)
    return redirect(url_for("post.get_all_posts"))


@post_bp.route("/delete/<int:post_id>/htmx", methods=["DELETE"])
def delete_one_post_htmx(post_id):
    post = post_model.get_post_by_id(post_id)
    if post is None:
        abort(404)

    post_model.delete_post(post_id)
    return ""
