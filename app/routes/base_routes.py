from flask import Blueprint

from app.views.base_views import render_home, render_root

base_bp = Blueprint("base", __name__, url_prefix="/")


@base_bp.route("/")
def root():
    return render_root()


@base_bp.route("/home")
def home():
    return render_home()
