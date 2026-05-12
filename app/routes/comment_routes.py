from flask import Blueprint

from app.views.comment_views import render_comment_list

comments_bp = Blueprint("comments", __name__, url_prefix="/comments")


@comments_bp.route("/list")
def get_all_comments():
    return render_comment_list()
